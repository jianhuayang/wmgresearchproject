**This repository contains the code and files pertaining to my WMG Research Project.**

The overall aim of the project was to investigate what VR content on TikTok can be used for educational purposes.

Using specific search terms (e.g. *virtual reality learning*), relevant videos were downloaded from TikTok.

Their content was categorised and a text analysis pipeline was implemented using dedicated Python libraries.
* The speech in the video was transcribed and saved in a text file.
* The most important words were identified using keyword extraction.

Note that the video in the downloads folder is simply a placeholder - please contact me (**samaksh.agarwal@warwick.ac.uk**) if you would like the complete dataset.

Here is a list of the required libraries required for the code to run:
* TensorFlow
* speech_recognition
* pydub (*FFmpeg also required*)
* spaCy

FFmpeg can be downloaded here: https://ffmpeg.org/download.html