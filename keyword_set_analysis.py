import text_analysis_pipeline as tap

def main(file1_name,file2_name):
    keywords_set = set()
    keywords2_set = set()

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

    print(keywords_set.intersection(keywords2_set))
    print(keywords_set.difference(keywords2_set))

if __name__ == "__main__":
    tap.main(1,3)
    tap.main(4,7,"keywords2.txt")
    main("keywords.txt", "keywords2.txt")