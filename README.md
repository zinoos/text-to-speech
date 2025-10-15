# 🗣️ Text-to-Speech with Hugging Face & Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/🤗_Transformers-Latest-orange)](https://huggingface.co/docs/transformers)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple **text-to-speech (TTS)** application built in Python using the [Hugging Face Transformers](https://huggingface.co/models) library.  
It converts written text into natural-sounding speech using the **Microsoft SpeechT5** model and **HiFi-GAN vocoder**.

---

## 🚀 Features
- 🎙️ Converts text into lifelike speech (English)
- ⚡ Fast inference using PyTorch
- 💾 Exports clean `.wav` audio files
- 🧠 Uses Hugging Face pretrained models (`SpeechT5`, `HiFi-GAN`)
- 🔁 Optional loop mode to generate multiple clips in one session

---

## 🧩 Tech Stack
- **Python** (3.10+)
- **PyTorch**
- **Transformers** (`microsoft/speecht5_tts`)
- **SoundFile**
- **SentencePiece**

---

## ⚙️ Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install torch transformers soundfile sentencepiece
