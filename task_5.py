def word_frequency():
    text = input("Enter a string: ")
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage:
if __name__ == "__main__":
    result = word_frequency()
    print(result)