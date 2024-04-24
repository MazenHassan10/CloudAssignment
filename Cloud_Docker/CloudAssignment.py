import nltk
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words('english'))

with open("paragraphs.txt" , "r") as file : 
    text = file.read()
    words = re.findall(r"[\w']+",text)
    filtered_words = [word for word in words if word.lower() not in stop_words ]

uniqe_words = list(set(filtered_words))

for word in uniqe_words : 
    print(word,":",filtered_words.count(word))
