from PyPDF2 import PdfReader
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.book import *
import nltk
import click
import inquirer


# The immutable core of code#
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))



def opening_file():
    start = input('Please state the name of pdf file that you want to open: ').lower()
    new_list = []
    try:
        question = input('Do you want to read all pdf or just page?: ').lower()
        if question == 'all':
            reader = PdfReader(start)
            for page in reader.pages:
                for word in word_tokenize(page.extract_text(), language='english'):
                    if word not in stop_words:
                        new_list.append(word.lower())
                                 
            return new_list
        
        elif question == 'page':
            number = input('Which page do you want to read?')
            reader = PdfReader(start)
            page = reader.pages[int(number)]
            new_list = [page.extract_text()]

            return new_list
            
    except ValueError:
        print('Invalid input. Please try again.')
    else:
        print('Invalid input. Please try again.')

def makes_concordance_function(open_pdf):
    """This function allow user to make concordance in pdf file.
    It's main core is opend_pdf function."""
    word = input('Please write word that you want to use in concordance: '
                 ).lower()
    text = Text(open_pdf)
    print(text.concordance(word))

def make_similarity(open_pdf):
    """This function allow user to make similarity in pdf file.
    It's main core is opend_pdf function."""
    word = input('Please write word that you want to use in similarity: '
                 ).lower()
    text = Text(open_pdf)
    print(text.similar(word))

def make_common_context(open_pdf):
    """This function allow user to make common_context in pdf file.
    It's main core is opend_pdf function."""
    word = input('Please write words that you want to use in common_context: '
                 )
    try:
        word = word.replace(',', '')
        word = word.split()
    except AttributeError:
        print('Invalid input. Please try again.')
    text = Text(open_pdf)
    
    print(text.common_contexts([word])) # need to work on that one


def make_count_word(open_pdf):
    """This function allow user to make count_word in pdf file.
    It's main core is opend_pdf function."""
    word = input('Please write word that you want to use in count_word: '
                 ).lower()
    text = Text(open_pdf)
    print(text.count(word))

def number_of_unique_words(open_pdf):
    """This function allow user to count number_of_unique_words in pdf file.
    It's main core is opend_pdf function."""
    text = Text(open_pdf)
    print(len(set(text)))

def number_of_common_words_in_total(open_pdf):
    """This function allow user to count number_of_common_words_in_total in pdf file.
    It's main core is opend_pdf function."""
    text = Text(open_pdf)
    print(len(text))


def working_on_data(open_pdf):
    """This function allow to work on data in pdf file.
    that was first edited in read_pdf function."""
    question = [
        inquirer.List('text editing',
                      message='How you want to work on your text?',
                      choices=['concordance', 'similarity', 'common_context',
                               'count_word', 'number_of_unique_words',
                               'number_of_common_words_in_total'],)
    ]
    answers = inquirer.prompt(question)
    
    if answers['text editing'] == 'concordance':
        makes_concordance_function(open_pdf)
    elif answers['text editing'] == 'similarity':
        make_similarity(open_pdf)
    elif answers['text editing'] == 'common_context':
        make_common_context(open_pdf)
    elif answers['text editing'] == 'count_word':
        make_count_word(open_pdf)
    elif answers['text editing'] == 'number_of_unique_words':
        number_of_unique_words(open_pdf)
    elif answers['text editing'] == 'number_of_common_words_in_total':
        number_of_common_words_in_total(open_pdf)
    
          






@click.group()
def cli():
    pass

@cli.command()
def read_pdf(): 
    """This function is allow user to read data from pdf file.
    It's main core is opend_pdf function.
    Summary of the code: 
    1. User can choose if he want to read all pdf or just one page.
    2. User can choose which page he want to read."""
    open_pdf = opening_file()
    working_on_data(open_pdf)

    
    

if __name__ == '__main__':
    cli()
