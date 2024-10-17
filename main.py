def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_char_count(text)
    sorted_dict = get_sorted_dict(character_count)
    # print(text)
    print(f"---Begin report of {book_path}---")
    print(f"There are {word_count} words in {book_path}") 

    # print(character_count)
    for c in sorted_dict:   
        char_key = c["char"]
        count_key = c["count"]
        print(f"The letter '{char_key}' has appeared '{count_key}' times")       

    

    


def get_book_text(path):
    print("attempting to open file")
    with open(path) as f:
        return f.read()
    print("file has been read")

def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    lowered_text = book.lower()
    char_dict = {}
    for c in lowered_text:
        if c.isalpha() == True:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1

    
    return char_dict



def sort_on(dict):
    return dict['count']

def get_sorted_dict(dict):
    char_list = [{'char': char, 'count': count} for char, count in dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list






main()
