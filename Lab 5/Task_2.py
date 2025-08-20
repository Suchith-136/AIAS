def analyze_sentiment(text):
    positive_words = {'awesome', 'excellent', 'good', 'great', 'fantastic', 'amazing', 'love', 'wonderful', 'positive', 'happy'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'hate', 'worst', 'negative', 'sad', 'disappointing', 'horrible'}

    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        return "Positive sentiment"
    elif neg_count > pos_count:
        return "Negative sentiment"
    else:
        return "Neutral sentiment"

if __name__ == "__main__":
    user_input = input("Enter your sentence: ")
    result = analyze_sentiment(user_input)
    print(result)