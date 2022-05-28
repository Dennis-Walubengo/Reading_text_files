# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(story):
    # [assignment] Add your code here
    file = open("story.txt", 'r')
    print("The file contents are:")
    print(file.read())
    # return "Hello World"


read_file_content("story")


def count_words():
    text = open("story.txt", 'r').read().split()
    # [assignment] Add your code here
    empty_dictionary = {}
    for line in text:
        line = line.strip()

        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in empty_dictionary:
                empty_dictionary[word] = empty_dictionary[word] + 1
            else:
                empty_dictionary[word] = 1
        for key in empty_dictionary:
            key = 0
        # return {"as": 10, "would": 20}
    print(" ")
    print(f'Unique word count is: {empty_dictionary}')


count_words()
