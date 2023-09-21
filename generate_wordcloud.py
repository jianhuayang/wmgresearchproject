from wordcloud import WordCloud

def generate_wordcloud(file_name, output_file):
    keywords = []
    frequencies = []

    with open(file_name, "r") as file:
        for line in file:
            words = line.strip().split(" ")

            keyword = " ".join(words[:-1])
            keywords.append(keyword)

            frequency = int(words[-1])
            frequencies.append(frequency)

    kw_dict = dict(zip(keywords, frequencies))

    wc = WordCloud(width= 700, height=400, max_words=15, max_font_size=90, background_color="white", colormap="gist_rainbow")
    wc.generate_from_frequencies(kw_dict)
    wc.to_file(output_file)

if __name__ == "__main__":
    generate_wordcloud("keywords.txt","keywords.png")
    generate_wordcloud("difference.txt", "difference.png")
