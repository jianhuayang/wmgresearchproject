from wordcloud import WordCloud

def main(file_name,output_file):
    with open(file_name,"r") as file:
        words = file.read().split()
    words_string = " ".join(words)

    wc = WordCloud(width=800, height=500, min_font_size=10, background_color="white", max_font_size=100, colormap="rainbow")
    wc.generate(words_string)
    wc.to_file(output_file)

if __name__ == "__main__":
    main("full_transcript.txt","set1.png")
    main("full_transcript2.txt","set2.png")
