def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    listed(letter_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    char_count = {}
    lower_case = text.lower()
    for char in lower_case:
        char_count[char] = char_count.get(char,0) + 1
    return char_count  

def listed(letter_count):
    quantity_list = []
    for letter, number in letter_count.items():
        quantity_dict = {"char" : letter, "num" : number}
        if letter.isalpha():
            quantity_list.append(quantity_dict)
    quantity_list.sort(reverse=True, key=sort_on)
    formatted(quantity_list)

def formatted(quantity_list):
    for item in quantity_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")
def sort_on(char_count):
    return char_count["num"]

main()