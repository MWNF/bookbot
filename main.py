def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = word_count(text)
    #print(f"Word count = {num_words}")
    char_count = char_counter(text)
    #print(f"Character count = {char_count}")
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    generate_report(char_counter(text))

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
        with open(path) as f:
            return f.read()

def char_counter(text):
    lowered_text = text.lower()
    char_totals = {}
    for chars in lowered_text:
        for char in chars:
            if char not in char_totals:
                char_totals[char] = 1
            else:
                char_totals[char] += 1
    return char_totals

def sort_on(dict):
    return dict["num"]

def generate_report(all_chars):
    #creating list of dictionaries, but only for alphabetic characters
    chars = [{"char": char, "num": count} for char, count in all_chars.items() if char.isalpha()]
    #sorting the list
    chars.sort(reverse=True, key=sort_on)
    for char_dict in chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")


main ()