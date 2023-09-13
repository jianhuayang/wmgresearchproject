from wordcloud import WordCloud

def keywords_generate(file_name,output_file):
    keywords = []
    frequencies = []

    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(" ")

            keyword = " ".join(parts[:-1])
            keywords.append(keyword)

            frequency = int(parts[-1])
            frequencies.append(frequency)

    kw_dict = dict(zip(keywords, frequencies))

    wc = WordCloud(width=800, height=500, background_color="white", colormap="rainbow")
    wc.generate_from_frequencies(kw_dict)
    wc.to_file(output_file)

def difference_generate(file_name, output_file):
    with open(file_name, "r") as file:
        words = file.read().split()

    words_string = " ".join(words)
    wc = WordCloud(width=800, height=500, max_font_size=125, background_color="white", colormap="rainbow")
    wc.generate(words_string)
    wc.to_file(output_file)

if __name__ == "__main__":
    keywords_generate("keywords.txt","set1.png")
    keywords_generate("keywords2.txt","set2.png")
    difference_generate("difference.txt", "difference.png")
