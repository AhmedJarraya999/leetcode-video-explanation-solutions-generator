from moviepy.editor import *
import os
from config import OUTPUT_DIR
from moviepy.config import change_settings

# Configure ImageMagick path
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})

# Helper to split long text into smaller slides
def split_text(text, max_chars=200):
    lines = []
    while len(text) > max_chars:
        split_index = text.rfind(" ", 0, max_chars)
        if split_index == -1:
            split_index = max_chars
        lines.append(text[:split_index])
        text = text[split_index:].strip()
    if text:
        lines.append(text)
    return lines

def generate_video(problem_text: str, explanation_text: str, audio_file: str, output_file="leetcode_video.mp4"):
    video_path = os.path.join(OUTPUT_DIR, "video", output_file)
    os.makedirs(os.path.dirname(video_path), exist_ok=True)

    # Problem slide
    problem_clip = TextClip(problem_text, fontsize=40, color='white', bg_color='black', size=(1280, 720), method='caption')
    problem_clip = problem_clip.set_duration(5)

    # Split explanation into smaller clips
    explanation_clips = []
    for segment in split_text(explanation_text, max_chars=200):
        clip = TextClip(segment, fontsize=30, color='white', bg_color='black', size=(1280, 720), method='caption')
        clip = clip.set_duration(5)  # duration per segment
        explanation_clips.append(clip)

    # Concatenate all clips
    video = concatenate_videoclips([problem_clip] + explanation_clips, method="compose")

    # Add narration
    narration = AudioFileClip(audio_file)
    video = video.set_audio(narration)  # do not override video duration

    # Export video
    video.write_videofile(video_path, fps=24)
    print(f"Video generated at: {video_path}")
    return video_path
