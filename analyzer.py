import re
from collections import Counter


def analyze_titles(titles):
    words = []

    for title in titles:
        if title:
            cleaned = re.findall(r'\b\w+\b', title.lower())
            words.extend(cleaned)

    counter = Counter(words)

    print("\n--- Repeated Words (>2 times) ---")
    for word, count in counter.items():
        if count > 2:
            print(f"{word} : {count}")
