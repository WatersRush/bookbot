import sys
from stats import get_num_words
from stats import dict_sort
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    path_to_file = sys.argv[1]    
    
    text = get_book_text(path_to_file)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    analyzed_data = dict_sort(text)
    for char_info in analyzed_data:
        char = char_info["char"]
        count = char_info["num"]
    
        print(f"{char}: {count}")
    print("============= END ===============")

main()