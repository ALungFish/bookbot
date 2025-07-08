def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    bob = num_of_words(text)
    noc = num_of_characters(text)
    print (f"{bob} words found in the document")
    print (noc)

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import num_of_words
     
from stats import num_of_characters   
main()