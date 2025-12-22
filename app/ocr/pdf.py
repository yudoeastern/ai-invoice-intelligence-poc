import subprocess, tempfile, os
import pdfplumber

def ocr_pdf(path: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as ocr_pdf:
        subprocess.run(
            ["ocrmypdf", "--force-ocr", path, ocr_pdf.name],
            check=True
        )

        text = ""
        with pdfplumber.open(ocr_pdf.name) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    os.remove(ocr_pdf.name)
    return text
