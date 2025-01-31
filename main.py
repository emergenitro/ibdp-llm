import os
# from scrapers.scraper_savemyexams import scrape_savemyexams

# from scrapers.scraper_compscihub import scrape_compscihub
# from scrapers.scraper_books import scrape_book_text
# from ocr.ocr_textbook import ocr_directory
# from model.prepare_dataset import collect_texts

# from model.train import train_llm

from model.inference import IBDPSubjectLLM
import shutil


def move_files_to_parent(subject_dir):
    """Move all files from subdirectories to the parent directory."""
    print(f"Processing {subject_dir}...")

    # Walk through all subdirectories
    for root, dirs, files in os.walk(subject_dir, topdown=False):
        # Skip if we're in the parent directory
        if root == subject_dir:
            continue

        # Move each file to parent directory
        for file in files:
            src_path = os.path.join(root, file)
            # Create unique filename if file already exists
            dst_path = os.path.join(subject_dir, file)
            counter = 1
            while os.path.exists(dst_path):
                name, ext = os.path.splitext(file)
                dst_path = os.path.join(subject_dir, f"{name}_{counter}{ext}")
                counter += 1

            try:
                shutil.move(src_path, dst_path)
                print(f"Moved: {src_path} -> {dst_path}")
            except Exception as e:
                print(f"Error moving {src_path}: {e}")


def main():
    # # 1. Scraping examples
    # scrape_savemyexams(
    #     "https://smearchive.pages.dev/dp/pdf-notes",
    #     "./data/biology_hl/savemyexams/",
    # )
    # scrape_compscihub(
    #     "http://ib.compscihub.net", "../data/computer_science_sl/compscihub/"
    # )
    # scrape_book_text(
    #     "https://somewhere.com/1984.txt", "../data/english_lit/texts/1984.txt"
    # )

    # # 2. OCR if needed
    # ocr_directory(
    #     "../data/economics_hl/ellie_tragakes_textbook_scans/",
    #     "../data/economics_hl/ellie_tragakes_textbook_ocr/",
    # )

    # # 3. Prepare dataset
    # subjects = [
    #     "econs_sl_2022",
    #     "bio_hl_2025",
    #     "bio_sl_2025",
    #     "chem_hl_2025",
    #     "chem_sl_2025",
    #     "econs_hl_2022",
    #     "ess_sl_2025",
    #     "mathsaa_hl",
    #     "mathsaa_sl",
    #     "mathsai_hl",
    #     "mathsai_sl",
    #     "physics_hl_2025",
    #     "physics_sl_2025",
    #     "psychology_hl",
    #     "psychology_sl",
    #     "bm_hl_2022",
    #     "bm_sl_2022",
    #     "ess_sl_2026",
    # ]
    # for subject in subjects:
    #     collect_texts(f"./data/{subject}", f"./data/{subject}_all.txt")

    # # 4. Train the LLM (fine-tune from GPT-2 or other base model)
    # train_llm()

    # 5. Inference
    ibdp_model = IBDPSubjectLLM("./checkpoints/ibdp_llm")
    print(
        ibdp_model.generate_answer("What is comparative advantage in economics?", 300)
    )


if __name__ == "__main__":
    main()
