# LLM for IBDP

## Overview
Hey everyone! I'm Karthik, a high school student who studies IBDP. I always felt that general LLMs like ChatGPT, Llama, etc., are too vague and ambigous for IB and is very frustrating if you have a question. That's why I made this LLM. **Y'all I had to pay $13 to host this due to limited upload capacity on Vercel, please vote!** :P

NOTE: I had to limit the number of tokens generated to 256 due to TERRIBLE computational resources that I'm working with.

Thanks!

## Website
You can visit the website here: [llm.karthik.lol](https://llm.karthik.lol)

## Features
- **Customized Responses:** Tailored to IBDP subjects and requirements.
- **Data-Driven:** Trained on hundreds of thousands of relevant texts.
- **User-Friendly:** Easy to integrate and use within various platforms.

## Project Structure
- **/scrapers/**  
  You can check out /scrapers/ for some of the scrapers I used to get data from the web. This basically contains Python scripts used to scrape and gather data from the web.

- **/model/**  
  I used a pretrained model, GPT2, and trained it on hundreds of thousands of texts which I've scraped from the web, using the py files in scrapers. Unfortunately, I am not too comfortable providing the datasets, which is why I have excluded it in the gitignore. I used `inference.py` to make the inference class so that it can use `generate_answers()` more easily! `prepare_dataset.py` to prepare the dataset, `train.py` to train the gpt2. I used huggingface's thing for this. Basically pretrained models and related resources.

- **/ocr/**
  I used an OCR when I had to convert textbooks to text in case they were not in text-readable format.

## Data
The model is trained on a vast dataset collected using the scrapers in the scrapers directory. Due to privacy and licensing concerns, the datasets are excluded from version control. Please refer to the .gitignore file for more details. Also, read the disclaimer below.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
NOTE: SOME OF THEM ARE NOT ALLOWED, AND THEREFORE WERE NOT ALLOWED. I STRONGLY SUGGEST YOU NOT USE THEM AS THEY ARE ILLEGAL TO USE AS THEY DO NOT ALIGN WITH THE TOS OF THE WEBSITES.

This is not the greatest LLM as it has been pretrained on GPT2 which is already known to be pretty bad. Nevertheless, it's something that works and I'm happy for that.