#Import the required libraries.
import text_analysis_pipeline as tap
import re

def main(import_file="keyphrases.txt", export_file="frequency_analysis.txt"):
    '''Identifies the keyphrases that occur most frequently in keyphrases.txt, excluding stop words. The results are written to a text file. '''
    frequency = {}
    keyphrase_doc = open(import_file, "r")
    keyphrase = keyphrase_doc.read().lower()

    #Use a regular expression to only include keywords that are between 3 and 15 characters.
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', keyphrase)

    #A list of stop words to be blacklisted.
    blacklisted = ['the', 'and', 'this', 'that', 'them', 'what', 'your', 'you']
    
    for word in match_pattern:
        if word not in blacklisted:
            count = frequency.get(word,0) #Return a value of 0 if the keyword is new.
            frequency[word] = count + 1 #Increment the frequency count for the keyword.

    #Sort the keywords by their frequency count in descending order.
    most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
    most_frequent_count = most_frequent.keys()
    
    with open(export_file,"w") as file:
        keywords_list = [(word,most_frequent[word]) for word in most_frequent_count]
        keywords = '\n'.join(' '.join(map(str, tpl)) for tpl in keywords_list)
        file.write(keywords)

if __name__ == "__main__":
    tap.main()
    main()
