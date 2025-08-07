import sys
import whisper

def transcribe(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    print(result["text"])
    return result["text"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file.wav>")
    else:
        transcribe(sys.argv[1])
