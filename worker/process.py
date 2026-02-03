import librosa
import soundfile as sf

def run(input_path, output_path):
    y, sr = librosa.load(input_path, mono=True)
    print(f"Loaded audio with {len(y)} samples at {sr} Hz")
    print(f"Duration: {len(y) / sr:.2f} seconds")
    sf.write(output_path, y, sr)