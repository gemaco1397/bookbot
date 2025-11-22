import sys
from stats import get_book_words
from stats import get_letters_used
from stats import sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        book = get_book_text(path)
        words_in_book = get_book_words(book)
        print(f"Found {words_in_book} total words")
        print("--------- Character Count -------")
        sorted_letters = sort_dictionary(get_letters_used(book))
        for letter in sorted_letters:
            if(letter["char"].isalpha() == True):
                print(f"{letter["char"]}: {letter["num"]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()