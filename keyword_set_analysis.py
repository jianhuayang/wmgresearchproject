import text_analysis_pipeline as tap

def main(file1_name,file2_name):
    file1 = open(file1_name)
    file2 = open(file2_name)

    keyphrases_set = set()
    keyphrases2_set = set()

    for word in file1.read().split():
        keyphrases_set.add(word.lower())

    for word in file2.read().split():
        keyphrases2_set.add(word.lower())

    print(keyphrases_set.intersection(keyphrases2_set))
    print(keyphrases_set.difference(keyphrases2_set))

if __name__ == "__main__":
    tap.main(1,10)
    tap.main(11,20,"keyphrases2.txt")
    main("keyphrases.txt", "keyphrases2.txt")