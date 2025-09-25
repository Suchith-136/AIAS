import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('movie_reviews-1.csv')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

# Apply cleaning to all string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_text)

# Save the cleaned DataFrame to a new CSV file
import numpy as np

# Tokenize and encode reviews using simple word embeddings (average of word vectors)
# For demonstration, we'll use a dummy embedding: assign a random vector to each word

# Identify the review column (assume it contains 'review' in its name)
review_col = None
for col in df.select_dtypes(include='object').columns:
    if 'review' in col.lower():
        review_col = col
        break

if review_col:
    # Build a vocabulary from all words in the reviews
    vocab = set()
    for text in df[review_col].fillna(''):
        vocab.update(text.split())
    vocab = list(vocab)
    word2idx = {word: idx for idx, word in enumerate(vocab)}
    np.random.seed(42)
    # Assign a random embedding vector (e.g., 50-dim) to each word
    embedding_dim = 50
    word_embeddings = {word: np.random.rand(embedding_dim) for word in vocab}

    def encode_review(text):
        words = text.split()
        vectors = [word_embeddings[word] for word in words if word in word_embeddings]
        if vectors:
            return np.mean(vectors, axis=0)
        else:
            return np.zeros(embedding_dim)
    
    # Apply encoding to each review, result is a numpy array for each review
    df['review_embedding'] = df[review_col].fillna('').apply(encode_review)
else:
    print("No review column found for tokenization and encoding.")
# Handle missing ratings (fill with median)
# Try to find a column that likely contains ratings
rating_col = None
for col in df.columns:
    if 'rating' in col.lower():
        rating_col = col
        break

if rating_col and pd.api.types.is_numeric_dtype(df[rating_col]):
    median_rating = df[rating_col].median()
    df[rating_col] = df[rating_col].fillna(median_rating)

# Normalize ratings to 0–1 scale if rating_col exists and is numeric
if rating_col and pd.api.types.is_numeric_dtype(df[rating_col]):
    min_rating = df[rating_col].min()
    max_rating = df[rating_col].max()
    if max_rating > min_rating:
        df[rating_col] = (df[rating_col] - min_rating) / (max_rating - min_rating)
    else:
        df[rating_col] = 0.0  # All ratings are the same

df.to_csv('movie_reviews-1_cleaned.csv', index=False)