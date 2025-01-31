# LLM for IBDP

## Overview
Hey everyone! I'm Karthik, a high school student who studies IBDP. I always felt that general LLMs like ChatGPT, Llama, etc., are too vague and ambigous for IB and is very frustrating if you have a question. That's why I made this LLM.

## Website
You can visit our website here: [ib-llm.vercel.app](https://ibllm.vercel.app)

## Project Structure
- **/scrapers/**  
  You can check out /scrapers/ for some of the scrapers I used to get data from the web.

- **/model/**  
  I used a pretrained model, GPT2, and trained it on hundreds of thousands of texts which I've scraped from the web, using the py files in scrapers. Unfortunately, I am not too comfortable providing the datasets, which is why I have excluded it in the gitignore. I used `inference.py` to make the inference class so that it can use `generate_answers()` more easily! `prepare_dataset.py` to prepare the dataset, `train.py` to train the gpt2. I used huggingface's thing

- **/ocr/**
  I used an OCR when I had to convert textbooks to text in case they were not in text-readable format.

## Disclaimer
NOTE: SOME OF THEM ARE NOT ALLOWED, AND THEREFORE WERE NOT ALLOWED. I STRONGLY SUGGEST YOU NOT USE THEM AS THEY ARE ILLEGAL TO USE AS THEY DO NOT ALIGN WITH THE TOS OF THE WEBSITES.

This is not the greatest LLM as it has been pretrained on GPT2 which is already known to be pretty bad. Nevertheless, it's something that works and I'm happy for that.