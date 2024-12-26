
def main():
    path = 'books/frankenstein.txt'
    text = get_text_from_book(path)
    count = get_word_count(text)
    print(f"--- Begin report of {path} ---")
    print(count, 'words found in the document\n')
    display_char_count(get_char_count(text))

def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(dict):
    return dict['num']

def display_char_count(chars):
    char_list = []
    for char in chars.keys():
        char_list.append({'name': char, 'num': chars[char]})
    char_list.sort(reverse=True, key=sort_on)
    for kvp in char_list:
        if kvp['name'].isalpha():
            print(f"The '{kvp['name']}' character was found {kvp['num']} times")

main()
