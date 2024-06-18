def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    gen_report(book_path, num_words, chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def gen_report(book, words, chars):
    chars_list = []
    print(f"--- Begin report of {book} ---")
    print("")
    print(f"There are {words} in {book}")
    print("")
    for char in chars:
        char_dict = {}
        if char.isalpha():
            char_dict["char"] = char
            char_dict["num"] = chars[char]
            chars_list.append(char_dict)

    chars_list.sort(reverse=True, key=sort_on)
    for char in chars_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()