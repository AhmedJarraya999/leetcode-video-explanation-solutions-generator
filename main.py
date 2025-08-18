from src.explanation_generator import generate_explanation
from src.tts_generator import text_to_speech
from src.video_generator import generate_video

# Read example problem
problem_text = open("examples/two_sum.txt").read()

# Generate explanation
explanation = generate_explanation(problem_text)
print("Generated Explanation:\n")
print(explanation)

# Convert explanation to speech
audio_file = text_to_speech(explanation)

# Generate video
video_file = generate_video(problem_text, explanation, audio_file)
