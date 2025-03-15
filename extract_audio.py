import sys
import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_path)
        video.close()
        return True
    except Exception as e:
        print(f"Error extracting audio: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a video file path")
        sys.exit(1)

    output_directory = "./audio/original"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = f"{output_directory}/audio_extracted.mp3"

    if extract_audio(sys.argv[1], output_path):
        print("Audio extraction completed successfully")
    else:
        print("Audio extraction failed")
        sys.exit(1)
