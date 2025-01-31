from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "google-bert/bert-large-cased-whole-word-masking"
)
tokenizer.save_pretrained("../checkpoints/ibdp_llm")
