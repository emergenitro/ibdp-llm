from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset
from torch.cuda import is_available


def tokenize_function(examples, tokenizer):
    return tokenizer(examples["text"], truncation=True, max_length=512)


def group_texts(examples):
    # Concatenate all texts
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])

    # We drop the small remainder, and just keep the truncated multiple of block_size
    total_length = (total_length // 512) * 512

    # Split by chunks of max_len
    result = {
        k: [t[i : i + 512] for i in range(0, total_length, 512)]
        for k, t in concatenated_examples.items()
    }

    # Create labels
    result["labels"] = result["input_ids"].copy()
    return result


def train_llm(
    model_name="gpt2",
    train_text_file="./data/all_subjects_combined.txt",
    output_dir="./checkpoints/ibdp_llm",
):
    device = "cuda" if is_available() else "cpu"
    print(f"Using device: {device}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if not tokenizer.pad_token:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

    # Load dataset
    raw_dataset = load_dataset("text", data_files={"train": train_text_file})

    # Tokenize
    tokenized_dataset = raw_dataset["train"].map(
        lambda x: tokenize_function(x, tokenizer), batched=True, remove_columns=["text"]
    )

    # Group texts
    lm_dataset = tokenized_dataset.map(group_texts, batched=True, batch_size=1000)

    # Data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=4,  # Reduced for GPU memory
        gradient_accumulation_steps=4,  # Effective batch size = 16
        num_train_epochs=3,
        logging_steps=100,
        save_steps=500,
        learning_rate=5e-5,
        warmup_steps=100,
        save_total_limit=2,
        fp16=True,  # Enable mixed precision
        gradient_checkpointing=True,  # Memory efficiency
        dataloader_num_workers=4,  # Parallel data loading
        remove_unused_columns=True,  # Memory efficiency
    )

    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=lm_dataset,
        data_collator=data_collator,
    )

    # Train and save
    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)


if __name__ == "__main__":
    train_llm()
