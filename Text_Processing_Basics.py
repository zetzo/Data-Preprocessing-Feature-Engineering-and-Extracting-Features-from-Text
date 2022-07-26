from collections import Counter

doc = "A very simple feature you can engineer from your document or documents is word counts. Perhaps the length of a sentence or document is meaningful for your prediction task, or maybe you're interested in eliminating the highest-count word."

doc_counter = Counter(doc.split())
print(doc_counter)

doc_lower = doc.lower()

doc_counter = Counter(doc_lower.split())
print(doc_counter)

doc_split_and_strip = [word.strip(".") for word in doc_lower.split()]

doc_counter = Counter(doc_split_and_strip)
print(doc_counter)

