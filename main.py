

char_counts = {}

def main1():
    with open('books/frankenstein.txt') as f:
        book = f.read()

    book = book.lower()
    for ch in book:
        char_counts[ch] = char_counts.get(ch, 0) + 1

    print(char_counts)
    print(char_counts[' '])   


main1()
