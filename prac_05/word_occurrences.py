"""
Word Occurrences
Estimate: 10 minutes
Actual:   21 minutes
"""

word_counts = {}
words_string = input("Text: ").lower()
words = words_string.split()
for word in words:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

max_word_length = max(len(key) for key in word_counts.keys())
for word, counts in sorted(word_counts.items()):
    print(f"{word:{max_word_length}} : {counts}")