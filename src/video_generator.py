from moviepy.editor import *
import os
from config import OUTPUT_DIR

def generate_video(problem_text: str, explanation_text: str, audio_file: str, output_file="leetcode_video.mp4"):
    video_path = os.path.join(OUTPUT_DIR, "video", output_file)
    os.makedirs(os.path.dirname(video_path), exist_ok=True)

    # Problem slide
    problem_clip = TextClip(problem_text, fontsize=40, color='white', bg_color='black', size=(1280, 720), method='caption')
    problem_clip = problem_clip.set_duration(5)

    # Explanation slide
    explanation_clip = TextClip(explanation_text, fontsize=30, color='white', bg_color='black', size=(1280, 720), method='caption')
    explanation_clip = explanation_clip.set_duration(10)

    # Concatenate clips
    video = concatenate_videoclips([problem_clip, explanation_clip])

    # Add narration
    narration = AudioFileClip(audio_file)
    video = video.set_duration(narration.duration)
    video = video.set_audio(narration)

    video.write_videofile(video_path, fps=24)
    print(f"Video generated at: {video_path}")
    return video_path
