import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import scipy.special
import tqdm

# Load your DataFrame
df = pd.read_csv('combined.csv')

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

# Function to compute sentiment scores
def do_text(text):
    try:
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        scores = {k: v for k, v in zip(model.config.id2label.values(), scipy.special.softmax(logits.numpy().squeeze()))}
        return scores['positive'], scores['negative'], scores['neutral']
    except:
        return 0, 0, 0

# Identify unique descriptions
unique_descriptions = df['Description'].unique()

# Dictionary to hold sentiment scores for unique descriptions
sentiment_scores = {}

# Compute sentiment scores for each unique description
for desc in tqdm.tqdm(unique_descriptions, desc="Computing sentiment scores"):
    sentiment_scores[desc] = do_text(desc)

# Map the computed sentiment scores back to the DataFrame
df['Positive'], df['Negative'], df['Neutral'] = zip(*df['Description'].map(sentiment_scores))

# Save the DataFrame with sentiment scores
df.to_csv('Sentiment.csv', index=False)
