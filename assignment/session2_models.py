"""
SESSION 2: GPT vs BERT vs T5
Demonstrating Transformers for Text Generation, Sentiment Analysis, and Paraphrasing.
"""

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def task1_gpt2_caption():
    print("=" * 60)
    print("TASK 1: GPT-2 Instagram Caption Generator")
    print("=" * 60)
    # Using pipeline for GPT-2 text generation
    caption_generator = pipeline('text-generation', model='gpt2')
    prompt = "Sunset vibes at the beach"
    results = caption_generator(
        prompt, 
        max_length=40, 
        num_return_sequences=1,
        temperature=0.8,
        pad_token_id=50256
    )
    caption = results[0]['generated_text']
    print(f"Prompt: {prompt}")
    print(f"Generated Caption: {caption}\n")
    return caption


def task2_bert_sentiment():
    print("=" * 60)
    print("TASK 2: BERT Sentiment Analysis for Zomato Review")
    print("=" * 60)
    # Using pipeline for sentiment analysis with standard BERT/DistilBERT
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    review = "The food was absolutely delicious and the delivery was super fast."
    result = sentiment_analyzer(review)
    print(f"Review: '{review}'")
    print(f"Sentiment Result: {result}\n")
    return result


def task3_t5_paraphrase():
    print("=" * 60)
    print("TASK 3: T5-base Sentence Paraphraser")
    print("=" * 60)
    # Using t5-base / t5-small model for text-to-text generation
    model_name = "t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    text = "BookMyShow makes movie ticket booking easy and fast."
    input_text = "paraphrase: " + text
    
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_length=60,
        num_beams=4,
        early_stopping=True
    )
    paraphrased = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Original Text: {text}")
    print(f"Paraphrased Text: {paraphrased}\n")
    return paraphrased


if __name__ == "__main__":
    task1_gpt2_caption()
    task2_bert_sentiment()
    task3_t5_paraphrase()
