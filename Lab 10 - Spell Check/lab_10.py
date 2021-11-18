import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

word_list = 0


def main():
    dictionary = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)

    dictionary.close()

    print("---Linear Search---")

    text = open("AliceInWonderLand200.txt")

    for line in text:
        result = split_line(line)
        word_list = result

        for item in word_list():



    text.close

print(word_list)


main()