from stats import word_count, char_dict, sorted_list_dict
import sys


def get_book_text(rel_file_path):
    with open(rel_file_path) as f: 
        file_contents = f.read()
    return file_contents
def main():
    #print(sys.argv[0])
    #print(sys.argv[1])
    #book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    words_in_book = word_count(contents)
    
    letter_dict = char_dict(contents)
   # print(letter_dict)
    sorted_list_d = sorted_list_dict(letter_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book} total words")
    print("--------- Character Count -------")
    for item in sorted_list_d:
        if item["key"].isalpha():
            print(f"{item["key"]}: {item["num"]}")
    print("============= END ===============")
main()
