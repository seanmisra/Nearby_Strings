# requires python 2.7 and above
import argparse


# from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


if __name__ == '__main__':
    # default word count and word
    word_count = 10

    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a string to match words against")
    parser.add_argument("-n", type=int, help="number of similar words to output")
    args = parser.parse_args()

    # option to input key_word via command-line
    key_word = args.word

    # option to input word count via command-line
    if args.n:
        word_count = args.n

    # get all words from /usr/share/dict/words
    all_words = []
    with open('/usr/share/dict/words') as word_file:
        for line in word_file:
            for word in line.split():
                all_words.append(word)

    # find levenshtein for each word in all_words
    # store key/value pairs in dictionary
    word_dictionary = {}
    for word in all_words:
        distance = levenshtein(key_word, word)
        word_dictionary[word] = distance

    # print first 10 values (w/ shortest distance)
    count = 0
    for key, value in sorted(word_dictionary.iteritems(), key=lambda (k, v): (v, k)):
        print key
        count += 1
        if count == word_count:
            break
