# Video to Text Transcription Project Documentation

## Overview
This project converts video files to text transcriptions using either Whisper or wav2vec models, with audio preprocessing and noise removal capabilities.

## Prerequisites
- Python 3.8 or higher
- ffmpeg
- Git
- Linux/Unix environment

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Transcribing-Video-to-Text
```

2. Make scripts executable:
```bash
chmod +x setup.sh generate_transcripts.sh
```

3. Create required directories:
```bash
mkdir -p videos audio/original audio/cleaned graphs/original graphs/cleaned output
```

## Project Structure

```
Transcribing-Video-to-Text/
├── audio/
│   ├── original/     # Extracted audio files
│   └── cleaned/      # Noise-reduced audio files
├── graphs/
│   ├── original/     # Original audio visualizations
│   └── cleaned/      # Cleaned audio visualizations
├── output/           # Generated transcripts
├── videos/           # Input video files
├── extract_audio.py  # Audio extraction script
├── preprocess_audio.py # Audio preprocessing
├── noise_removal.py  # Noise reduction
├── main.py          # Main transcription script
├── utils.py         # Utility functions
└── setup.sh         # Setup script
```

## Usage

1. Place your video file in the `videos` directory

2. Run the transcription with Whisper (recommended):
```bash
./generate_transcripts.sh ./videos/your_video.mp4 whisper
```

   Or with wav2vec (requires model.pth):
```bash
./generate_transcripts.sh ./videos/your_video.mp4 wav2vec
```

## Pipeline Steps

1. **Audio Extraction**: 
   - Extracts audio from video file
   - Saves as MP3 in audio/original/

2. **Preprocessing**: 
   - Normalizes audio
   - Generates visualizations
   - Saves plots in graphs/original/

3. **Noise Removal**: 
   - Reduces background noise
   - Generates cleaned audio visualizations
   - Saves in audio/cleaned/ and graphs/cleaned/

4. **Transcription**: 
   - Converts audio to text using selected model
   - Saves transcript in output/

## Output Files

- **Transcripts**: Found in `output/` directory
  - `whisper_transcript.txt` or
  - `wav2vec_transcript.txt`

- **Audio Files**:
  - Original: `audio/original/audio_extracted.mp3`
  - Cleaned: `audio/cleaned/cleaned_audio.mp3`

- **Visualizations**:
  - Original audio waveform and spectrogram in `graphs/original/`
  - Cleaned audio waveform and spectrogram in `graphs/cleaned/`

## Troubleshooting

1. **Dependency Issues**:
   ```bash
   ./setup.sh
   ```

2. **Permission Denied**:
   ```bash
   chmod +x setup.sh generate_transcripts.sh
   ```

3. **Missing Directories**:
   ```bash
   mkdir -p videos audio/original audio/cleaned graphs/original graphs/cleaned output
   ```

## Notes
- Whisper method works out of the box
- wav2vec requires model.pth file in root directory
- First run downloads required models (~2GB)
