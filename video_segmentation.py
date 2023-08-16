import pixellib
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5") 
segment_image.process_video("./downloads/video1.mp4", show_bboxes=True, frames_per_second=15, output_video_name="output_video.mp4")