import spacy
from textblob import TextBlob
from pdf2image import convert_from_path
from pdf2image import convert_from_bytes

import pytesseract
from PIL import Image
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import subprocess


# file_path = "dataset/i_have_a_dream.txt"

# Download the spaCy English language model
# !python -m spacy download en_core_web_sm

# Download the spaCy English language model
# subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def preprocessWithSpacy(file_path):
    # Load the English NLP model
    # nlp = spacy.load("en_core_web_sm")

    # Read the content of the dataset file
    
    with open(file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    # Process the text with Spacy
    doc = nlp(text_data)

    # View the processed tokens and entities
    for token in doc[:10]:  # Displaying the first 10 tokens
        print(token.text, token.pos_, token.dep_)

    # If you want to see the named entities detected by Spacy
    for ent in doc.ents:
        print(ent.text, ent.label_)
        
def preprocess_text(text):
    
     # Load the English NLP model
    # nlp = spacy.load("en_core_web_sm")
    
    doc= nlp(text)
    # Tokenize the text, remove stopwords, and filter out non-alphabetic words
    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]

    return words
        
        
def preprocessWithTextBlob(file_path):    


    # Read the content of the dataset file
    # file_path = "dataset/i_have_a_dream.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    # Create a TextBlob object
    blob = TextBlob(text_data)

    # Print the raw text
    print("Raw Text:")
    print(blob.raw)

    # Print tokenized words
    print("\nTokenized Words:")
    print(blob.words)

    # Print noun phrases
    print("\nNoun Phrases:")
    print(blob.noun_phrases)

    # Print sentences
    print("\nSentences:")
    print(blob.sentences)

    # Perform sentiment analysis
    print("\nSentiment Analysis:")
    print("Polarity:", blob.sentiment.polarity)
    print("Subjectivity:", blob.sentiment.subjectivity)
    

def extractTextFromPdf(uploaded_file):
    # Convert PDF to images
    images = convert_from_bytes(uploaded_file.read(), dpi=300)

    # Read the content of the dataset file
    pdf_file_path = "dataset/i_have_a_dream.pdf"   
    
    # Convert the PDF to a list of images
    images = convert_from_bytes(uploaded_file)
    
    combined_text = ""
    # Iterate through each page/image and perform OCR
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='eng')  # 'eng' for English, you can change the language code
        combined_text += text
        # print(f"Text from page {i + 1}:\n{combined_text}")
        # image.show()

    return combined_text


def ocrOfUploadedPdf(uploaded_file):
    # Convert PDF to images
    images = convert_from_bytes(uploaded_file.read(), dpi=300)

    # # Read the content of the dataset file
    # pdf_file_path = "dataset/i_have_a_dream.pdf"   
    
    # # Convert the PDF to a list of images
    # images = convert_from_path(pdf_file_path)
    
    combined_text = ""
    # Iterate through each page/image and perform OCR
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='eng')  # 'eng' for English, you can change the language code
        combined_text += text
        # print(f"Text from page {i + 1}:\n{combined_text}")
        # image.show()
    
    print('combind_data :: ', combined_text)
    
    words = preprocess_text(combined_text)
    
     # Calculate word frequencies
    word_freq = pd.Series(words).value_counts()

    # Create a DataFrame with unique words and their counts
    df_word_freq = pd.DataFrame({'Word': word_freq.index, 'Count': word_freq.values})

    # Sort the DataFrame by count in descending order
    df_word_freq = df_word_freq.sort_values(by='Count', ascending=False)
    
    # Filter the DataFrame to include only rows where Count is greater than 10
    filtered_df = df_word_freq[df_word_freq['Count'] >= 10]

    return filtered_df, combined_text
    
    
def ocrOfPdf():
    # Read the content of the dataset file
    pdf_file_path = "dataset/i_have_a_dream.pdf"   
    
    # Convert the PDF to a list of images
    images = convert_from_path(pdf_file_path)
    
    combined_text = ""
    # Iterate through each page/image and perform OCR
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='eng')  # 'eng' for English, you can change the language code
        combined_text += text
        # print(f"Text from page {i + 1}:\n{combined_text}")
        # image.show()
    
    print('combind_data :: ', combined_text)
    
    words = preprocess_text(combined_text)
    
     # Calculate word frequencies
    word_freq = pd.Series(words).value_counts()

    # Create a DataFrame with unique words and their counts
    df_word_freq = pd.DataFrame({'Word': word_freq.index, 'Count': word_freq.values})

    # Sort the DataFrame by count in descending order
    df_word_freq = df_word_freq.sort_values(by='Count', ascending=False)
    
    # Filter the DataFrame to include only rows where Count is greater than 10
    filtered_df = df_word_freq[df_word_freq['Count'] >= 10]

    return filtered_df
    
def generate_wordcloud(df):
    print("Word Cloud Fucntion is called.")

    # Convert the DataFrame to a dictionary
    word_freq_dict = dict(zip(df['Word'], df['Count']))
    # # Generate a word cloud
    # wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(df.set_index('Word')['Count'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq_dict)


    # # Display the generated word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()