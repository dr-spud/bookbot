def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    

    print(text)
    print(f"word count: {word_count}") 


def get_book_text(path):
    print("attempting to open file")
    with open(path) as f:
        return f.read()
    print("file has been read")

def get_word_count(book):
    words = book.split()
    return len(words)



        


   



main()
