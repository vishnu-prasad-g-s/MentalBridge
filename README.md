# 🌉 MentalBridge

> An offline AI mental health companion for India — built on Gemma 4, running entirely on your device.

**No server. No data leaving. No internet needed. Just someone to listen — in your language.**

[![Gemma 4](https://img.shields.io/badge/Gemma_4-E2B-green)](https://ollama.com/library/gemma4)
[![Ollama](https://img.shields.io/badge/Runs_on-Ollama-blue)](https://ollama.com)
[![HuggingFace](https://img.shields.io/badge/Model-HuggingFace-orange)](https://huggingface.co/vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 🌍 The Problem

In India, **197 million people** live with a mental health condition. Only **1 in 10** ever receives help — not because they don't want it, but because saying the words out loud feels impossible. The stigma is heavier than the illness. The nearest psychiatrist is hours away. And every app that could help sends your most private thoughts to a server somewhere.

MentalBridge was built to change that.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Warm AI Chat** | Gemma 4 responds warmly in your language. Short, human, one gentle question at a time |
| 📵 **100% Offline** | Runs entirely on-device via Ollama. No internet needed after setup |
| 🗣️ **Multilingual** | Tamil, Hindi, Telugu, Kannada, English — auto-detected and matched |
| 🚨 **Crisis Detection** | Instantly surfaces Indian helplines when distress signals are detected |
| 🫧 **Breathing Exercise** | Guided 4-7-8 technique with animated real-time visual |
| 🌊 **Ripple Pond** | Real wave physics simulation for meditative grounding |
| 🫧 **Pop Your Thoughts** | ACT therapy gamified — pop calm thoughts, let anxious ones drift |
| 🌱 **5-4-3-2-1 Grounding** | Clinical grounding protocol with visual feedback |
| 📊 **Mood Tracker** | Daily mood logging with history |
| 🔒 **Zero Data Stored** | No account, no analytics, no data collection of any kind |

---

## 🚀 Quick Start

### macOS

**Step 1 — Install Ollama**

Download from [ollama.com](https://ollama.com) and install.

**Step 2 — Download Gemma 4 E2B**

Open Terminal and run:
```bash
ollama pull gemma4:e2b
```

**Step 3 — Download MentalBridge**

Download the ZIP from the [releases page](https://github.com/vishnu-prasad-g-s/MentalBridge/releases), unzip it.

Right-click the unzipped folder → select **"New Terminal at Folder"**, then run:
```bash
bash START.sh
```

**Step 4 — Open in browser**

MentalBridge opens automatically. If not, go to:
```
http://localhost:8080
```

---

### Windows

**Step 1 — Install Ollama**

Download from [ollama.com/download/windows](https://ollama.com/download/windows) and run the installer.

**Step 2 — Download Gemma 4 E2B**

Open Command Prompt (search "cmd" in Start menu) and run:
```cmd
ollama pull gemma4:e2b
```

**Step 3 — Download MentalBridge**

Download the ZIP from the [releases page](https://github.com/vishnu-prasad-g-s/MentalBridge/releases) and unzip it.

Open two Command Prompt windows:

**Window 1 — Start Ollama with CORS:**
```cmd
set OLLAMA_ORIGINS=* && ollama serve
```

**Window 2 — Start the web server:**
```cmd
cd path\to\mentalbridge_download
python -m http.server 8080
```

> 💡 Requires Python. Download from [python.org](https://python.org) — check "Add to PATH" during install.

**Step 4 — Open in browser**

Open Chrome or Edge and go to:
```
http://localhost:8080
```

---

## 🤖 Model & Fine-tuning

MentalBridge uses **Gemma 4 E2B** as the base model with a custom system prompt engineered for:
- Cultural awareness (Indian family dynamics, NEET pressure, arranged marriage stress)
- Strict language matching (responds only in the user's language)
- Crisis escalation (surfaces Indian helplines immediately)
- Therapeutic response structure (reflect → validate → one gentle question)

We also fine-tuned a **Gemma 4 E2B LoRA adapter** using **Unsloth** on 192 Indian mental health conversations — 177 from a Kaggle mental health dataset and 15 handcrafted examples covering uniquely Indian scenarios in Tamil, Hindi and English.

**Fine-tuning results:**
- Training loss: **8.72 → 1.41** over 72 steps
- 3 epochs, learning rate 2e-4, LoRA rank 16
- Published on HuggingFace: [vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned](https://huggingface.co/vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned)

---

## 🏗️ Architecture

```
User (Browser)
    ↕ HTTP (localhost:8080)
HTML/CSS/JS App (index.html)
    ↕ REST API (localhost:11434)
Ollama (local inference server)
    ↕ Model weights (on disk)
Gemma 4 E2B (7.2GB GGUF)
```

Everything runs locally. No external calls. No telemetry.

---

## 🧰 Tech Stack

- **AI Model:** Google Gemma 4 E2B via Ollama
- **Fine-tuning:** Unsloth on Kaggle T4 GPU
- **Frontend:** Pure HTML/CSS/JavaScript (no frameworks)
- **Inference:** Ollama local HTTP API
- **Serving:** Python built-in HTTP server
- **Games:** Canvas 2D API with Verlet wave physics
- **Voice:** Web Speech API

---

## 📞 Indian Mental Health Helplines

| Organisation | Number | Hours |
|---|---|---|
| iCall | 9152987821 | Mon–Sat 8am–10pm |
| Vandrevala Foundation | 1860-2662-345 | 24/7 |
| NIMHANS | 080-46110007 | National referrals |
| Snehi | 044-24640050 | Tamil speaking |

---

## ⚠️ Disclaimer

MentalBridge is **not a substitute for professional mental health care.** It is a first-aid companion designed to provide support and guide users toward professional help. If you are in immediate crisis, please call iCall at **9152987821** immediately.

---

## 🏆 Hackathon

Built for the **Gemma 4 Good Hackathon 2026** on Kaggle.

Tracks: Health & Sciences · Digital Equity & Inclusivity · Ollama Special Track · Unsloth Special Track

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

*Made with care in Chennai, India 🇮🇳*
