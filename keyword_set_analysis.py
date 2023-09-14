def main(file1_name, file2_name):
    '''Compares two sets of keywords from text files, identifying the set difference between them. The result is then written to a text file.'''
    keywords1_set = set() #The keywords from the more popular set.
    with open(file1_name, "r") as file:
        for line in file:
            words = line.strip().split(" ")
            keyword = " ".join(words[:-1])
            keywords1_set.add(keyword)

    keywords2_set = set() #The keywords from less popular set.
    with open(file2_name, "r") as file:
        for line in file:
            words = line.strip().split(" ")
            keyword = " ".join(words[:-1])
            keywords2_set.add(keyword)

    #Identify common keywords that only appear in the more popular set.
    difference = keywords1_set.difference(keywords2_set)
    with open("difference.txt", "w") as file:
        for kw in difference:
            file.write(kw + "\n")

if __name__ == "__main__":
    main("keywords1.txt", "keywords2.txt")