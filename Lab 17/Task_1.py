import pandas as pd
import string

# Load the CSV file
df = pd.read_csv('social_media.csv')

# Define a list of common English stopwords
stopwords = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
    'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should',
    "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
    'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
    'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
    'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
])

# Function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove punctuation and special symbols
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove non-alphanumeric characters (special symbols)
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    # Lowercase and split into words
    words = text.lower().split()
    # Remove stopwords
    filtered_words = [word for word in words if word not in stopwords]
    # Join back into a string
    return ' '.join(filtered_words)

# Apply cleaning to 'post_text' column
if 'post_text' in df.columns:
    df['post_text'] = df['post_text'].apply(clean_text)

# Save the cleaned DataFrame back to CSV (optional, remove if not needed)
# Handle missing values in 'likes' and 'shares' columns by filling with 0
for col in ['likes', 'shares']:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# Convert 'timestamp' column to datetime and extract hour and weekday features
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['hour'] = df['timestamp'].dt.hour
    df['weekday'] = df['timestamp'].dt.weekday

# Remove duplicate/spam posts so that only two unique posts remain in 'post_text'
if 'post_text' in df.columns:
    # Drop duplicates based on 'post_text'
    df_unique = df.drop_duplicates(subset=['post_text'])
    # Keep only the first two unique posts
    df_unique = df_unique.head(2)
    df_unique.to_csv('social_media_cleaned.csv', index=False)
else:
    df.to_csv('social_media_cleaned.csv', index=False)