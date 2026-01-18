from fastapi import FastAPI, UploadFile, File
import tempfile, shutil, os

from app.ocr.image import ocr_image
from app.ocr.pdf import ocr_pdf
from app.ocr.doc import ocr_doc

from app.llm.qwen_cleaner import qwen_clean_text
from app.llm.qwen_invoice import extract_invoice_semantic, extract_amounts
from app.service.extractor import normalize_invoice

app = FastAPI(title="Invoice OCR API (POC)")

@app.post("/ocr/invoice")
async def ocr_invoice(file: UploadFile = File(...)):
    suffix = file.filename.lower()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        if suffix.endswith((".png", ".jpg", ".jpeg")):
            raw_text = ocr_image(tmp_path)
        elif suffix.endswith(".pdf"):
            raw_text = ocr_pdf(tmp_path)
        elif suffix.endswith(".docx"):
            raw_text = ocr_doc(tmp_path)
        else:
            return {"error": "Unsupported file type"}

        clean_text = qwen_clean_text(raw_text)
        llm_candidates = extract_invoice_semantic(clean_text)
        # invoice = normalize_invoice(llm_candidates)
        amounts = extract_amounts(clean_text)
        invoice = normalize_invoice(clean_text, amounts)


        return {
            "invoice": invoice
        }

    finally:
        os.remove(tmp_path)
