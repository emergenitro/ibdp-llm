import os
import fitz
import glob


def extract_text_from_pdf(pdf_path):
    text = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text.append(page.get_text())
    return "\n".join(text)


def collect_texts(root_data_dir, output_txt):
    """
    Traverse root_data_dir, extract text from PDFs, gather text files,
    and compile them into a single large text file for each subject.
    """
    with open(output_txt, "x", encoding="utf-8") as out_f:
        for root, dirs, files in os.walk(root_data_dir):
            for file in files:
                path = os.path.join(root, file)
                if file.lower().endswith(".pdf"):
                    pdf_text = extract_text_from_pdf(path)
                    out_f.write(f"\n--- FILE: {path} ---\n")
                    out_f.write(pdf_text + "\n")
                elif file.lower().endswith(".txt"):
                    with open(path, "r", encoding="utf-8") as in_f:
                        out_f.write(f"\n--- FILE: {path} ---\n")
                        out_f.write(in_f.read() + "\n")
