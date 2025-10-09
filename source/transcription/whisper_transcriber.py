from pathlib import Path
import subprocess
import tempfile

from faster_whisper import WhisperModel

class Whisper:
    def __init__(self, model_size: str = 'medium', device: str = 'cpu', compute_type: str = 'int8'):
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def _convert_to_wav(self, input_path: str) -> str:
        """Перекодовує будь-який аудіофайл у 16 кГц WAV."""
        output_path = Path(tempfile.gettempdir()) / (Path(input_path).stem + "_temp.wav")
        subprocess.run([
            "ffmpeg", "-y", "-i", input_path,
            "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le",
            str(output_path)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return str(output_path)

    def transcribe(self, audio_path: str) -> str:
        """Транскрибує файл"""
        wav_path = self._convert_to_wav(audio_path)

        segments, info = self.model.transcribe(wav_path, beam_size=5, vad_filter=True, language='uk', temperature=0.0, condition_on_previous_text=False)
        text = " ".join([s.text for s in segments])

        return text