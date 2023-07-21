from transformers import AutoTokenizer, AutoModelWithLMHead
from transformers import pipeline

tokenizer_sentiment = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")

model_sentiment = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-emotion")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_emotion(text):
  input_ids = tokenizer_sentiment.encode(text + '</s>', return_tensors='pt')

  output = model_sentiment.generate(input_ids=input_ids,
               max_length=2)

  dec = [tokenizer_sentiment.decode(ids) for ids in output]
  label = dec[0]
  return label

def summarize(text):
    return summarizer(text, max_length=130, min_length=30, do_sample=False)