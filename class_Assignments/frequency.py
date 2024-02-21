#!/usr/bin/python3
"""
Purpose: Test Frequency Analyses
"""

sentence = "Python is a wonderful language we can solve any computational problem with this language"

words = sentence.split()

word_counts = {}


for word in words:
    
    if word in word_counts:
        word_counts[word] += 1
    
    else:
        word_counts[word] = 1
print(word_counts)


print("Word frequency:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
    

