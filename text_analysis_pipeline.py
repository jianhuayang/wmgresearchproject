#Import all the required libraries.
import speech_recognition as sr
from pydub import AudioSegment
import os
from pathlib import Path
import spacy
import pytextrank

dir_path = "./downloads"
num_videos = sum(1 for element in os.scandir(dir_path) if element.is_file())

#Choose which videos from the dataset should be fed into the pipeline.
start_video = 1
end_video = 2

for i in range(start_video,end_video+1):
    file = "video" + str(i)
    file_path = f"./downloads/{file}.mp4"
    
    #Load the mp4 file and extract the audio into an audio file.
    video = AudioSegment.from_file(f"{file_path}", format = "mp4")

    #Ensure the audio file is in the correct format for speech recognition.
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2) 
    audio.export("audio.wav", format="wav")

    #Load the audio file and extract the speech from it.
    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_text = r.record(source)

    text = r.recognize_google(audio_text,language="en-US")

    #Write the transcript of the speech to a text file.
    file_name = "transcript.txt"

    with open(file_name, "w") as file:
        file.write(text)

    #Load the spaCy model in order to perform keyword extraction.
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(Path("transcript.txt").read_text(encoding="utf-8"))

    #Save the keywords from each video to a single text file.
    file_name = "keywords.txt"

    with open(file_name,"a") as file:
        keywords = [phrase.text for phrase in doc._.phrases if phrase.rank >=0] #Excludes individual words that convey no meaning, such as pronouns.
        keyword_string = '\n'.join(keywords)
        file.write(keyword_string)
