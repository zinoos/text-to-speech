# ---- Imports ----
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import torch
import soundfile as sf

# ---- Load model & vocoder ----
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# ---- Dummy speaker embedding (random voice) ----
speaker_embeddings = torch.randn(1, 512)

# ---- Function ----
def again():
    text = input("What do you want to say:\n")
    inputs = processor(text=text, return_tensors="pt")

    with torch.no_grad():
        speech = model.generate_speech(
            inputs["input_ids"],
            speaker_embeddings,
            vocoder=vocoder
        )

    sf.write("output.wav", speech.numpy(), 16000)
    print("✅ Saved as output.wav — should now actually speak")

    if input("Generate another? (y/n): ").lower() == "y":
        again()

again()
