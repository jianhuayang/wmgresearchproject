from scenedetect import open_video, SceneManager, AdaptiveDetector, FrameTimecode
def main(start_video=1, end_video=10):

    for i in range(start_video,end_video+1):
        #The file path should follow the naming convention of the saved videos.
        file = "video" + str(i)
        file_path = f"./downloads/{file}.mp4"

        video = open_video(file_path)
        sm = SceneManager()
        sm.add_detector((AdaptiveDetector()))
        sm.detect_scenes(video)

        scenes = sm.get_scene_list(start_in_scene=True) 
        num_scenes = len(scenes)
        total_length = 0

        for scene in scenes: 
            scene_length = scene[1].get_seconds() - scene[0].get_seconds()
            total_length+=scene_length

        avg_scene_length = round(total_length/num_scenes, 2)

        print(num_scenes,avg_scene_length)

if __name__ == "__main__":
    main()