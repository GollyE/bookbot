def get_book_text(rel_file_path):
    with open(rel_file_path) as f: 
        file_contents = f.read()
    return file_contents
def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    print(contents)
 
main()
