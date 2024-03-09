from gtts import gTTS
import pygame
import tempfile
import os

# Function to get user input for language, text, and preview
def get_user_input():
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language code (e.g., 'en' for English, 'hi' for Hindi): ")
    preview_option = input("Do you want to preview the speech before downloading? (yes/no): ")
    
    return text, language, preview_option.lower() == 'yes'

# Get user input
text, language, preview_option = get_user_input()

# Create a gTTS object with the specified language
tts = gTTS(text, lang=language)

# Create a temporary file to store the speech
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
    temp_filename = temp_mp3.name
    tts.save(temp_filename)

# Initialize the pygame mixer
pygame.mixer.init()

# Load and play the speech for preview
pygame.mixer.music.load(temp_filename)
pygame.mixer.music.play()

# Wait for the audio to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Clean up the audio playback
pygame.mixer.quit()

# Prompt the user to decide whether to download
if preview_option:
    download_option = input("Do you want to download the speech as an audio file? (yes/no): ")
    if download_option.lower() == 'yes':
        output_filename = input("Enter the filename to save the speech (e.g., output.mp3): ")
        os.rename(temp_filename, output_filename)
        print(f'Speech saved as {output_filename}')
else:
    # If no preview, assume the user wants to download
    output_filename = input("Enter the filename to save the speech (e.g., output.mp3): ")
    os.rename(temp_filename, output_filename)
    print(f'Speech saved as {output_filename}')

# Clean up the temporary audio file if not downloading
if not preview_option:
    os.remove(temp_filename)
