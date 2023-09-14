from scenedetect import open_video, SceneManager, AdaptiveDetector
import pandas as pd

def main(start_video=1, end_video=40):
    '''
    Analyses the subset of videos from the specified file path in order to determine the number of scenes and average scene length of each video.
    The results are then written to the video_data.csv file.
    '''
    avg_scene_length_list = []
    num_scenes_list = []

    for i in range(start_video,end_video+1):
        #The file path should follow the naming convention of the saved videos.
        file = "video" + str(i)
        file_path = f"./downloads/{file}.mp4"

        video = open_video(file_path)
        sm = SceneManager()
        sm.add_detector((AdaptiveDetector()))
        sm.detect_scenes(video)
        scenes = sm.get_scene_list(start_in_scene=True) #Ensure that a video with no scene changes has at least one scene.

        num_scenes = len(scenes)
        num_scenes_list.append(num_scenes)
        total_length = 0

        #Calculate the total length of the video by summing up the length of each scene.
        for scene in scenes: 
            #Calculate the scene length by subtracting the start time from the end time.
            scene_length = scene[1].get_seconds() - scene[0].get_seconds() 
            total_length+=scene_length

        #Calculate the average scene length of the video.
        avg_scene_length = round(total_length/num_scenes, 2)
        avg_scene_length_list.append(avg_scene_length)
    
    df = pd.read_csv("video_data.csv", index_col=0)
    df["Number of Scenes"] = num_scenes_list
    df["Average Scene Length"] = avg_scene_length_list
    df.to_csv("video_data.csv", index=False)

if __name__ == "__main__":
    main()