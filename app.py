import streamlit as st
from ocr_preprocessing import ocrOfPdf, ocrOfUploadedPdf, generate_wordcloud, extractTextFromPdf


st.title("OCR using Tesseract")

# Process Steps
st.sidebar.title("Process Steps")
st.sidebar.markdown("- Step 1: Load PDF using the upload section.")
st.sidebar.markdown("- Step 2: View the extracted text, word cloud, and word count table.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF successfully uploaded!")

    # Analyze the text and get word frequencies
    word_freq_table, combined_text = ocrOfUploadedPdf(uploaded_file)
    # word_freq_table = ocrOfPdf()

    # Extract the text from the pdf
    # extracted_text = extractTextFromPdf(uploaded_file)

    # Display text
    st.subheader("Extracted Text")
    st.write(combined_text)

    # Word Count Table
    st.subheader("Word Count Table")
    st.write(word_freq_table)

    # # Display word cloud
    st.subheader("Word Cloud")
    st.write(generate_wordcloud(word_freq_table))

    