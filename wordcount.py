# put your code here.
def word_count(filename):
    """ Break file contents into words and return the word count.

    """

    your_file = open(filename)
    words = your_file.read()
    words = words.split()

    words_counted = {}
    for word in words:
        words_counted[word] = words_counted.get(word, 0) + 1

    for word, count in words_counted.iteritems():
        print word, count


word_count("twain.txt")
