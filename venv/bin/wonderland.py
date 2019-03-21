def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, "r", encoding = "utf-8") as book:
            text = book.read()
    except FileNotFoundError:
        print("We could not find a book in your current working directory with the name, you have specified.")
    else:
        #Count the number of words in the file
        #i.e: split the string into parts whenever you encounter a space in it
        words = text.split()
        return(str(len(words)))
    return("0")

book_list = []
book_list.append("moby_dick.txt")
book_list.append("alice.txt")
book_list.append( "siddharta.txt")
book_list.append("little_women.txt")

for book in book_list:
    print(book + " contains approx. " + count_words(book) + " words.")




