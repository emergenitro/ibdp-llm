import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from .subject_classifier import subject_guard


class IBDPSubjectLLM:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.model.eval()

    @torch.no_grad()
    def generate_answer(self, prompt, max_new_tokens=128):
        # if not subject_guard(prompt):
        #     return "sorry cannot respond"

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        output_ids = self.model.generate(
            input_ids=input_ids,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
