#import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import nltk

#data = pd.read_csv("/Users/jakobahlberg/cleaned_data3.csv")
#print(data.head(10))

#for i in range(100):
    #tokens = nltk.word_tokenize(data["description.text"][i])
    #print(f"Tokens for row {i}: {tokens}")

import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Load the CSV data file
data = pd.read_csv("/Users/jakobahlberg/cleaned_data3.csv")

# Define stop words in English and Swedish
stop_words_en = set(stopwords.words('english'))
stop_words_sv = set(stopwords.words('swedish'))

# Loop through the rows in the DataFrame and preprocess the text
results = []
for i in range(len(data)):
    # Tokenize the text
    tokens = nltk.word_tokenize(data["description.text"][i])
    
    # Lowercase the text
    tokens = [token.lower() for token in tokens]
    
    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Remove stop words in English and Swedish
    tokens = [token for token in tokens if token not in stop_words_en and token not in stop_words_sv]
    
    # Check if the word "blockchain" is in the preprocessed tokens
    if "blockchain" in tokens:
        results.append(i)
        
        # Print the preprocessed tokens for this row
        print(f"Preprocessed tokens for row {i}: {tokens}")
        
        # Exit the loop if 10 rows containing "blockchain" have been found
        if len(results) == 10:
            break

        #hej