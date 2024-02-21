"""
Assignment
==========
choose a large sentence greater than 150 words and perform the following
1) character frequency analyses
    a) case sensitive
        {
            'P': 1,
            'y': 2,
            't : 5
            ....
        }
    b) case insensitive
        {
            'p': 2,
            'y': 2,
            't : 5
            .....
        }
        HINT: str.lower()
2) word frequency analyses
    a) case sensitive
    b) case insensitive
    HINT: str.split()

3) cleansed_words frequency analyses
        HINT: string module -> string.punctuation
    a) case sensitive
    b) case insensitive

    Are you coming?  --> ['Are', 'you', 'coming']

"""
import string

sentence = "In the quiet town, there lived a man named Jack. Jack was known for his love of fishing. He would often spend hours by the serene lake, patiently waiting for a bite. Jack's favorite pastime was fishing for bass. He had a special spot by the old oak tree where he claimed the biggest catches were found. Sometimes, JACK would bring his friends along, sharing his fishing secrets with them. They would sit together, swapping stories and enjoying the tranquility of the outdoors. JACK's passion for fishing was contagious, inspiring others to take up the hobby. Even on cloudy days, Jack would venture out, determined to reel in a big one. For Jack, fishing wasn't just a hobby; it was a way of life—a way to connect with nature and find inner peace."

words = sentence.split()

word_counts = {}
c_word_counts = {}
letter_count = {}
c_letter_count = {}
word_list = []

for word in words:

    if word in string.punctuation:
        pass
    else:
        word_list.append(word)
    
    if word in word_counts:

        word_counts[word] += 1
    
    else:
        word_counts[word] = 1
    #case sensitive
    for i in word :

        if i in letter_count:
            letter_count[i] +=1
        else:
            letter_count[i] = 1
 
for word in words:
    word = word.lower() 
    if word in c_word_counts:
        c_word_counts[word] += 1
    
    else:
        c_word_counts[word] = 1

    for j in word.lower() :
        if j in c_letter_count:
            c_letter_count[j] +=1
        else:
            c_letter_count[j] = 1


print(f"a) case sensitive : {letter_count} \n")

print(f"b) case insensitive : {c_letter_count} \n")

print(f" a) Word case sensitive : {word_counts}\n")

print(f"b)Word case insensitive :{c_word_counts}\n")

print(f"{word_list}")
    