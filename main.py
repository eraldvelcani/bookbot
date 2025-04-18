import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents 

def read_book(path):
    with open(path) as f:
        return f.read()

from stats import num_of_words
from stats import char_counter
from stats import sort_dict

def get_path(book):
    return print(open(book))

def main():
    path = sys.argv[1]
    chars_sorted_list = sort_dict(char_counter(read_book(path)))
    #print(f"{num_of_words(path)} words found in the document")
    #print(char_counter(read_book(path)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(path)} total words")
    print("--------- Character Count -------")
    for i in chars_sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
