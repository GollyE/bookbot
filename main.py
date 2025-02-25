from stats import word_count, char_dict

def get_book_text(rel_file_path):
    with open(rel_file_path) as f: 
        file_contents = f.read()
    return file_contents
def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    words_in_book = word_count(contents)
    print(f"{words_in_book} words found in the document")
    letter_dict = char_dict(contents)
    print(letter_dict)
main()
