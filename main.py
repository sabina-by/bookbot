from stats import (
    get_num_words ,
    get_num_char,
    get_sorted_list
)
import sys

def main():
    try:
        book_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_char(text)
    char_list = get_sorted_list(char_count)
    print_report(book_path, num_words, char_list)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        if not entry["char"].isalpha():
            continue
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
