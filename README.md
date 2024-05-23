**To run the application, follow below steps**
- Install python in your pc or laptop.
- Clone the application to your local environment
  - **git clone https://github.com/datascientistshiva/text_preprocessing.git**
- **cd text_preprocessing/**
- Create a virtual environment
  - **python -m venv /venv-name** or **python3 -m venv /venv-name**
- To install all the library from requirements.txt file.
  - **pip install -r requirements.txt**
- To run the python application.
  - **streamlit run app.py**


**About the application**
***Structure of the application***
1. **requirements.txt**
    - spacy : ***Designed for NLP task and handles large amount of data efficiently.***
    - streamlit : ***Build application for Data sharing.*** 
    - pytesseract : ***Used to extract text from images.***
    - Pillow : ***Used for text preprocessing and manipulation.***
    - pandas : ***Load and preprocess the data***
    - wordcloud : ***Create a cloud like structure from the important words from the text data.***
    - matplotlib : ***Data visualization tools.***
    - fastapi : ***Used to create an REST api***

2. **app.py**
    - This is the main python file which is responsible to run our streamlit application.
    - Contains image upload section.
    - Extract text from the images using pytessaract library.
    - Created word count table and word cloud.
    
3. **ocr-preprocessing.py**
   - All the task like load the pdf, extract the text from pdf and clean it.
   - Pytessaract is used to extract text from the uploaded images.
   - Tokenize, removal of stop words and punctuation marks.
   - Remove numeric data and other symbols.
   - Generate word count table and word cloud.
   - 
   

