import warnings
import librosa
import soundfile as sf
from plots import *
import os

def load_audio(audio_path):
    try:
        audio, sr = librosa.load(audio_path, sr=None, mono=True)
        return audio, sr
    except Exception as e:
        print(f"Error loading audio: {str(e)}")
        return None, None

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    
    audio_path = './audio/original/audio_extracted.mp3'
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        exit(1)

    audio, sr = load_audio(audio_path)
    if audio is None:
        print("Failed to load audio")
        exit(1)

    output_directory = "./graphs/original"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    plot_audio(audio, sr, output_directory, title='Original Audio')
    normalized_audio = librosa.util.normalize(audio)
    plot_audio(normalized_audio, sr, output_directory, title='Normalized Audio')
    plot_spectrogram(audio, sr, output_directory, title='Spectrogram')
