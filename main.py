def get_book_text(rel_file_path):
    with open(rel_file_path) as f: 
        file_contents = f.read()
    return file_contents
def word_count(input_text):
    num_of_words = len(input_text.split())
    return num_of_words
def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    words_in_book = word_count(contents)
    print(f"{words_in_book} words found in the document")
main()
