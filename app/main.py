import os
import whisper

def transcribe_all(directory="data/recording"):
    model = whisper.load_model("small")
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            path = os.path.join(directory, filename)
            print(f"Transcribing: {filename}")
            result = model.transcribe(path)
            with open(f"{directory}/{filename}.txt", "w") as f:
                f.write(result["text"])
            print(f"Saved transcription to {filename}.txt")

if __name__ == "__main__":
    transcribe_all()
