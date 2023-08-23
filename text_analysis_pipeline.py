#Import all the required libraries.
import speech_recognition as sr
from pydub import AudioSegment
import os
from pathlib import Path
import spacy
import pytextrank
import re

#Choose which videos from the dataset should be fed into the pipeline.
start_video = 1
end_video = 10

def audio_extraction(file_path):
    '''Loads the video from a given file path and extracts the audio into a wav file, ensuring it is in the correct format.'''
    video = AudioSegment.from_file(file_path, format = "mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2) 
    audio.export("audio.wav", format="wav")

def speech_recognition():
    '''Loads the audio file and extracts the speech from it, writing the transcript to a text file.'''
    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_text = r.record(source)

    text = r.recognize_google(audio_text,language="en-US") #Uses the Google Speech Recognition model.

    file_name = "transcript.txt"
    with open(file_name, "w") as file:
        file.write(text)

def keyphrase_extraction():
    '''Performs keyphrase extraction on the transcript using the spaCy model, appending all unique keyphrases to a text file.'''
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(Path("transcript.txt").read_text(encoding="utf-8"))

    file_name = "keyphrases.txt"
    with open(file_name,"a") as file:
        keyphrases_list = [phrase.text for phrase in doc._.phrases if phrase.rank >=0] #Excludes keyphrases that convey no meaning, such as pronouns.
        keyphrases = '\n'.join(keyphrases_list) + '\n'
        file.write(keyphrases)

def main():
    '''The output of the pipeline is a text file containing all the keyphrases from the entire subset of specified videos.'''
    for i in range(start_video,end_video+1):
        #The file path should follow the naming convention of the saved videos.
        file = "video" + str(i)
        file_path = f"./downloads/{file}.mp4"

        audio_extraction(file_path)
        speech_recognition()
        keyphrase_extraction()

if __name__ == "__main__":
    main()