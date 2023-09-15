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

    wc = WordCloud(width= 600, height=300, max_words=20, background_color="white", colormap="rainbow")
    wc.generate_from_frequencies(kw_dict)
    wc.to_file(output_file)

def difference_generate(file_name, output_file):
    with open(file_name, "r") as file:
        words = file.read().split()

    words_string = " ".join(words)
    wc = WordCloud(width=600, height=300, stopwords=None, max_font_size=100, background_color="white", colormap="rainbow")
    wc.generate(words_string)
    wc.to_file(output_file)

if __name__ == "__main__":
    keywords_generate("keywords.txt","keywords.png")
    difference_generate("difference.txt", "difference.png")
