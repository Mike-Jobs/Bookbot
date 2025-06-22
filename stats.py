
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def characters(book):
    character=book.lower()
    char_count = {}
    for i in character:
        if i in char_count:
            char_count[i] = char_count[i] + 1
        else:
            char_count[i] = 1
    return char_count

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    book=get_book_text(book_path)
    count = book.split()
    print(f"Found {len(count)} total words")

    character_counts = characters(book)
    return (character_counts)
    
    print(f"Found {count} total words")
    

#main()
def sort(character_counts):
    sort_on = []
    for i in character_counts:
        if i.isalpha():
            sort_on.append({"char": i, "num": character_counts[i]})
    sort_on.sort(key=lambda item: item["num"], reverse=True)
    print("--------- Character Count -------")
    for item in sort_on:
        print(f"{item['char']}: {item['num']}")
sort(main())