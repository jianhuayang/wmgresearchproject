#Import all the required libraries to perform the text analysis.
import speech_recognition as sr
from pydub import AudioSegment
from pathlib import Path
import spacy
import pytextrank

#Load the mp4 file and extract the audio into an audio file.
video = AudioSegment.from_file("./downloads/video1.mp4", format = "mp4")

#Ensure the audio file is in the correct format for speech recognition.
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2) 
audio.export("audio.wav", format="wav")

#Load the audio file and extract any speech from it.
r = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio_text = r.record(source)

text = r.recognize_google(audio_text,language="en-US")

#Save a transcript of the speech as a text file.
file_name = "transcript.txt"

with open(file_name, "w") as file:
    file.write(text)

#Load the spaCy model in order to perform keyword extraction.
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")

doc = nlp(Path("transcript.txt").read_text(encoding="utf-8"))
for phrase in doc._.phrases:
    print(phrase.text, phrase.rank, phrase.count) #A higher rank value means the phrase is more relevant.

