**This repository contains all the code and files relating to my research project supported by Warwick Manufacturing Group (WMG).**

The overall aim of the project was to investigate the key factors affecting the popularity of VR-related educational videos on TikTok.

The speech and video content of videos within the dataset was analysed in order to identify certain trends.

Relevant videos were identified using general keyword search terms (e.g. *virtual reality learning*).

The text analysis pipeline for each video included the following stages:
* Video Transcription (using the *pydub* and *speech_recognition* libraries)
* Punctuation Restoration (using the *rpunct* library)
* Keyword Extraction (using the *yake* library)

Wordclouds were then generated from the extracted keywords as a data visualisation technique.

Furthermore, the transitions in each video were analysed in order to record the number of distinct scenes and calculate the average scene length (this was done using the *pyscenedetect* library).

Statistical analysis was then performed on all the recorded data using *pandas* and *numpy*, after which the results were plotted using *matplotlib*.

Note that the video in the downloads folder is simply a placeholder - please contact me (**samaksh.agarwal@warwick.ac.uk**) if you would like the complete dataset.

FFmpeg (required for video transcription) can be downloaded here: https://ffmpeg.org/download.html