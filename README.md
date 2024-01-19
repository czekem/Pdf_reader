Pdf_reader

Pdf_reader is a Python script that allows you to read and analyze text from PDF files. It uses the PyPDF2: https://pypi.org/project/PyPDF2/ library to read PDF files and the NLTK: https://www.nltk.org/ library to perform natural language processing (NLP) tasks.
Features

    Read text from all or a specific page of a PDF file.
    Tokenize text into words and sentences.
    Remove stop words.
    Perform concordance, similarity, common context, word count, number of unique words, and number of common words in total.

Usage

To use Pdf_reader, first install the required libraries:

pip install PyPDF2 nltk

Then, run the following command:

python pdf_reader.py

This will open a prompt where you can choose whether to read all or a specific page of a PDF file. If you choose to read all pages, the script will print the text of the entire file. If you choose to read a specific page, the script will prompt you for the page number.

Once you have chosen how to read the text, the script will perform the following tasks:

    Tokenize the text into words and sentences.
    Remove stop words.
    Ask you how you want to work on the text. You can choose from the following options:
        concordance: Prints the concordance of a given word.
        similarity: Prints the most similar words to a given word.
        common_context: Prints the common contexts of a given word.
        count_word: Prints the number of occurrences of a given word.
        number_of_unique_words: Prints the number of unique words in the text.
        number_of_common_words_in_total: Prints the total number of words in the text.

Examples

Here are some examples of how to use Pdf_reader:

# Read all pages of a PDF file and print the concordance of the word "the"
python pdf_reader.py --concordance the

# Read page 10 of a PDF file and print the similarity of the word "love"
python pdf_reader.py --page 10 --similarity love

# Read all pages of a PDF file and print the common contexts of the words "love" and "hate"
python pdf_reader.py --common_context love hate

# Read all pages of a PDF file and print the number of occurrences of the word "freedom"
python pdf_reader.py --count_word freedom

# Read all pages of a PDF file and print the number of unique words
python pdf_reader.py --number_of_unique_words

# Read all pages of a PDF file and print the total number of words
python pdf_reader.py --number_of_common_words_in_total
