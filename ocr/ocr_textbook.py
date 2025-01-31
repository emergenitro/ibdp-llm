import pytesseract
from pdf2image import convert_from_path


def pdf_to_text(pdf_path, output_txt_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)

    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    pdf_path = "path/to/your/pdf_file.pdf"
    output_txt_path = "path/to/output_text_file.txt"
    pdf_to_text(pdf_path, output_txt_path)
