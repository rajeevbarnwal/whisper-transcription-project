import os
import whisper

def transcribe(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    return result["text"]

def transcribe_all(directory="data/recording"):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            path = os.path.join(directory, filename)
            print(f"Transcribing: {filename}")
            text = transcribe(path)
            output_file = f"{path}.txt"
            with open(output_file, "w") as f:
                f.write(text)
            print(f"Saved to: {output_file}")

if __name__ == "__main__":
    transcribe_all()
