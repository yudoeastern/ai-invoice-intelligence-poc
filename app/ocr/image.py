from PIL import Image
import pytesseract

def ocr_image(path: str) -> str:
    image = Image.open(path)
    return pytesseract.image_to_string(image, lang="ind+eng")
