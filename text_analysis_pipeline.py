#Import all the required libraries.
from pathlib import Path
from pydub import AudioSegment
import speech_recognition as sr
import yake

def clear_file(file_name):
    '''Clear the text file.'''
    with open(file_name,'w') as file:
        pass

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

    try:
        text = r.recognize_google(audio_text,language="en-US") #Uses the Google Speech Recognition model.

        file_name = "transcript.txt"
        with open(file_name, "w") as file:
            file.write(text)

    except sr.UnknownValueError:
        print("Could not transcribe.")

def keyphrase_extraction(file_name):
    '''Performs keyphrase extraction on the transcript using the spaCy model, appending all unique keyphrases to a text file.'''
    with open("transcript.txt", "r") as file:
        words = file.read().split()

    words_string = "".join(word for word in words) + " "

    kw_extractor = yake.KeywordExtractor()
    
    with open(file_name,"a") as file:
        keyphrases = '\n'.join(words_string) + '\n'
        file.write(keyphrases)

def main(start_video=1, end_video=5, file_name="keyphrases.txt"):
    '''The output of the pipeline is a text file containing all the keyphrases from the entire subset of specified videos.'''
    clear_file(file_name)
    for i in range(start_video,end_video+1):
        #The file path should follow the naming convention of the saved videos.
        file = "video" + str(i)
        file_path = f"./downloads/{file}.mp4"

        audio_extraction(file_path)
        speech_recognition()
        keyphrase_extraction(file_name)

if __name__ == "__main__":
    main(1,1)