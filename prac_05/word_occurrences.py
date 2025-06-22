"""
Word Occurrences
Estimate: 10 minutes
Actual:    minutes
"""

word_counts = {}
words_string = input("Text: ").lower()
words = words_string.split()
for word in words:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1