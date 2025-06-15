import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np


# Load model and tokenizer
def load_model(model_path=None):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model.eval()
    return model, tokenizer

def predict(text, model, tokenizer, threshold=0.2):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.sigmoid(logits).squeeze().numpy()
    indexes_above_threshold = [i for i, val in enumerate(probabilities) if val > threshold]
    return indexes_above_threshold, probabilities

def map_predictions_to_labels(indexes, labels_list):
    return [labels_list[i] for i in indexes]