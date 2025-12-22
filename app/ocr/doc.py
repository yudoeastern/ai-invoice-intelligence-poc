from docx import Document

def ocr_doc(path: str) -> str:
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])
