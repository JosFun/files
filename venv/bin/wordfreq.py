import pygal

def get_word_histogram(*book_names):
    """Counts the word frequency of each word found in the text being stored under the filename book_name."""
    book_words = list()
    dictionary = dict()

    for book_name in book_names:
        try:
            with open(book_name) as book:
                data = book.read()
                book_words = data.split()
            book.close()
        except FileNotFoundError:
            print("We could not find you book. Please give it another try.")
        else:
            for word in book_words:
                # first, check whether or not the item is already contained in the dictionary
                # if it is: get its frequency and then delete the entry in the dictionary
                if word in dictionary:
                    freq = dictionary.get(word)
                    dictionary.pop(word)
                    dictionary[word] = freq + 1
                else:
                    dictionary[word] = 1


    return(dictionary)

def make_hist(word_dict, text_name, min_occurence):
    """Creates the histogram, showing the quantites of each majority word in the dictionary.
       A majority word is a word that occurs at least min_occurence times in the text. """
    hist = pygal.Bar()
    hist.title = "Counting the word frequencies in " + text_name
    hist.x_title = "Words"
    hist.y_title = "Frequency of each word"

    # Sort the dictionary
    word_dict = {k: v for k,v in sorted(word_dict.items(), key = lambda x : x [ 1 ])} #Remember that dict.items represents a list of tupels

    data = {"word":[], "count":[]} # Of course this is a dictionary as well
    for key in word_dict.keys():
        if word_dict.get(key) > min_occurence:
            data["word"].append(key)
            data["count"].append(word_dict.get(key))

    hist.x_labels = data["word"]
    hist.add(text_name, data["count"])
    hist.render_to_file('word_freq.svg')

make_hist(get_word_histogram("alice.txt", "moby_dick.txt", "little_women.txt"), "Alice in Wonderland, Moby Dick, Little Women", 100)
