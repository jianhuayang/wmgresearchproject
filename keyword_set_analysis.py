def main(file1_name,file2_name):
    keywords_set = set() #The more popular set.
    keywords2_set = set() #The less popular set.

    with open(file1_name, "r") as file:
        for line in file:
            words = line.strip().split(" ")
            keyword = " ".join(words[:-1])
            keywords_set.add(keyword)

    with open(file2_name, "r") as file:
        for line in file:
            words = line.strip().split(" ")
            keyword = " ".join(words[:-1])
            keywords2_set.add(keyword)

    #Identify common keywords that only appear in the more popular set.
    difference = keywords_set.difference(keywords2_set)
    with open("difference.txt", "w") as file:
        for kw in difference:
            file.write(kw + "\n")

if __name__ == "__main__":
    main("keywords.txt", "keywords2.txt")