import nltk
import numpy as np
import random
import string


from bs4 import BeautifulSoup 


import bs4 as bs
import urllib.request
import re
print("Hello, I am GoogleSearch. Give me the URL of a webpage you want answers from here ->  ")
raw_html = urllib.request.urlopen(input())
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
    article_text += para.text

article_text = article_text.lower()
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
article_sentences = nltk.sent_tokenize(article_text)
article_words = nltk.word_tokenize(article_text)
wnlemmatizer = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    return [wnlemmatizer.lemmatize(token) for token in tokens]

punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))

greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity        
def generate_response(user_input):
    bot_response = ''
    article_sentences.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        bot_response = bot_response + "I am sorry, I could not understand you!"
        return bot_response
    else:
        bot_response = bot_response + article_sentences[similar_sentence_number]
        return bot_response

word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
all_word_vectors = word_vectorizer.fit_transform(article_sentences)
similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
similar_sentence_number = similar_vector_values.argsort()[0][-2]
continue_dialogue = True

while(continue_dialogue == True):
    print(" Ask your question:  ")
    user_text = input()
    user_text = user_text.lower()
    if user_text != 'bye':
        if user_text == 'thanks' or user_text == 'thank you very much' or user_text == 'thank you':
            continue_dialogue = False
            print("Google Search: Most welcome")
        else:
            if generate_greeting_response(user_text) != None:
                print("Google Search: " + generate_greeting_response(user_text))
            else:
                print("Google Search: ", end="")
                print(generate_response(user_text))
                article_sentences.remove(user_text)
    else:
        continue_dialogue = False
        print("Google Search: Good bye and take care. Come back again if you want to know something...")

