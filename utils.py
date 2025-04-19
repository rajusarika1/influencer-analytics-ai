from transformers import pipeline

classifier = pipeline("zero-shot-classification")
labels = ["travel", "food", "fashion", "fitness", "beauty", "tech"]

def categorize_post(text):
    result = classifier(text, labels)
    return result['labels'][0]

def calculate_engagement(likes, views):
    return (likes / views) * 100
