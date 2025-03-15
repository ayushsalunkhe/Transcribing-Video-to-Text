import torch
import torchaudio
import os
from torchaudio.pipelines import WAV2VEC2_ASR_BASE_960H

# Force CPU
if torch.cuda.is_available():
    torch.cuda.is_available = lambda : False

class GreedyCTCDecoder(torch.nn.Module):
    def __init__(self, labels, blank=0):
        super().__init__()
        self.labels = labels
        self.blank = blank

    def forward(self, emission: torch.Tensor) -> str:
        indices = torch.argmax(emission, dim=-1)
        indices = torch.unique_consecutive(indices, dim=-1)
        indices = [i for i in indices if i != self.blank]
        return "".join([self.labels[i] for i in indices])

def load_wav2vec2_asr_model(model_path):
    try:
        device = "cpu"  # Force CPU usage to avoid CUDA issues
        model = WAV2VEC2_ASR_BASE_960H.get_model()
        if os.path.exists(model_path):
            model.load_state_dict(torch.load(model_path, map_location=device))
        model.eval()
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None

def transcribe_audio(model, audio_path):
    try:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        waveform, sample_rate = torchaudio.load(audio_path)
        if sample_rate != WAV2VEC2_ASR_BASE_960H.sample_rate:
            waveform = torchaudio.functional.resample(
                waveform, sample_rate, WAV2VEC2_ASR_BASE_960H.sample_rate)

        waveform = waveform.to("cpu")

        with torch.no_grad():
            emission, _ = model(waveform)

        decoder = GreedyCTCDecoder(labels=WAV2VEC2_ASR_BASE_960H.get_labels())
        transcript = decoder(emission[0])
        return transcript
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return ""
