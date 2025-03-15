import librosa
from pydub import AudioSegment
import os
from plots import *
import noisereduce as nr
from scipy.io import wavfile

def process_audio(audio_path):
    try:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        audio, sr = librosa.load(audio_path, sr=None)
        noise_reduced_audio = nr.reduce_noise(y=audio, sr=sr)
        return noise_reduced_audio, sr
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return None, None

if __name__ == "__main__":
    audio_path = './audio/original/audio_extracted.mp3'
    noise_reduced_audio, sr = process_audio(audio_path)
    if noise_reduced_audio is None:
        print("Failed to process audio")
        exit(1)

    output_directory = "./graphs/cleaned"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    plot_audio(noise_reduced_audio, sr, output_directory, title='Cleaned_Audio')
    plot_spectrogram(noise_reduced_audio, sr, output_directory, title='Cleaned_Audio_Spectrogram')

    output_directory = "./audio/cleaned"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    wavfile.write(f'{output_directory}/cleaned_audio.wav', sr, noise_reduced_audio)

    audio = AudioSegment.from_wav(f'{output_directory}/cleaned_audio.wav')
    audio.export(f'{output_directory}/cleaned_audio.mp3', format='mp3')
