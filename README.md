# 🌉 MentalBridge — AI Mental Health Companion for India

> **Gemma 4 Good Hackathon Submission** · Track: Digital Equity & Inclusivity · Health & Sciences · Unsloth

[![HuggingFace Model](https://img.shields.io/badge/🤗%20HuggingFace-mentalbridge--gemma4--E2B-green)](https://huggingface.co/vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned)
[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Training%20Notebook-blue)](https://www.kaggle.com/YOUR_KAGGLE_LINK)
[![Live Demo](https://img.shields.io/badge/Live-Demo-orange)](https://YOUR_DEMO_LINK)

---

## 🌿 The Problem

197 million Indians live with a mental health condition. **Only 1 in 10 ever gets help.**

Not because they don't want it — because saying the words out loud feels impossible. The stigma is heavier than the illness itself. They suffer in silence. Every single day.

Existing AI mental health tools fail India because:
- They respond in Western therapy language ("practice self-care", "here are 5 tips...")
- They don't understand IIT pressure, CA exam failure, arranged marriage anxiety
- They send conversations to remote servers — destroying privacy
- They don't speak Tamil, Hindi, or Telugu naturally

## 🌉 The Solution

MentalBridge is a **privacy-first, offline, multilingual mental health first-aid companion** powered by a fine-tuned Gemma 4 model running entirely on-device via Ollama.

### What makes it different:
- 🔒 **100% offline** — conversations never leave the device
- 🗣️ **Multilingual** — English, Tamil, Hindi, Telugu, Kannada
- 🇮🇳 **Culturally calibrated** — fine-tuned on Indian mental health scenarios
- 🆘 **Safe escalation** — surfaces Indian helplines (iCall, Vandrevala) for crisis
- 🎮 **Therapeutic tools** — breathing exercises, mood tracking, grounding games, realistic pond meditation

---

## 🧠 Architecture

```
User Input (any Indian language)
         ↓
  MentalBridge App (index.html)
         ↓
  Ollama Local Server (localhost:11434)
         ↓
  Gemma 4 E2B — Fine-tuned LoRA Adapter
  (vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned)
         ↓
  Culturally-aware response
  + crisis detection
  + Indian helpline routing
```

---

## 🤖 Fine-tuning Details (Unsloth Prize Track)

| Parameter | Value |
|---|---|
| Base model | `unsloth/gemma-4-E2B-it` (Gemma 4, 2B params) |
| Fine-tuning method | LoRA via Unsloth |
| LoRA rank | r=16, alpha=16 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Dataset size | 192 examples |
| Training epochs | 3 |
| Total steps | 72 |
| Final training loss | 0.843 |
| Platform | Kaggle (2x Tesla T4) |
| Training time | ~5 minutes |

### Dataset Composition
- **Kaggle mental health intents dataset** (filtered, ~178 examples)
- **Custom Indian scenarios** (14 hand-crafted examples):
  - NEET/CA/UPSC exam failure + family shame
  - Arranged marriage pressure
  - Tamil (`நான் மிகவும் தனிமையாக உணர்கிறேன்`)
  - Hindi (`मुझे हर रात रोना आता है`)
  - Domestic violence signals
  - Job loss shame
  - Software engineer burnout (IT culture)
  - Crisis escalation to iCall

### HuggingFace Model
🤗 **[vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned](https://huggingface.co/vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned)**

---

## 📱 App Features

| Screen | Description |
|---|---|
| 💬 Talk | AI conversation powered by fine-tuned Gemma 4 |
| 🪷 Mood | Daily mood tracking with history |
| 🫧 Breathe | 4-7-8 breathing technique with real countdown |
| 🎮 Calm | Ripple Pond (physics simulation), Pop Thoughts (CBT defusion), 5-4-3-2-1 grounding |
| 📞 Help | Indian mental health resources — iCall, Vandrevala, NIMHANS, Snehi |

---

## 🚀 Running Locally

### Prerequisites
- [Ollama](https://ollama.ai) installed
- Gemma 4 E2B pulled

### Steps
```bash
# 1. Install Ollama (one time)
# Download from: https://ollama.ai

# 2. Pull Gemma 4 E2B
ollama pull gemma4:e2b

# 3. Start Ollama
ollama serve

# 4. Open the app
# Just open index.html in your browser
# Or serve it:
python3 -m http.server 8080
# Then visit: http://localhost:8080
```

### Using the Fine-tuned Model (Advanced)
```bash
# 1. Download the LoRA adapter from HuggingFace:
# https://huggingface.co/vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned

# 2. The model runs as LoRA adapter on top of gemma4:e2b base
# For demo purposes, the app uses gemma4:e2b with the MentalBridge system prompt
```

---

## 📁 Repository Structure

```
mentalbridge/
├── index.html              # Complete app (single file, works offline)
├── mentalbridge.ipynb      # Fine-tuning notebook (Kaggle/Unsloth)
├── README.md               # This file
└── dataset/
    └── indian_scenarios.json  # Custom Indian training data
```

---

## 🏆 Prize Track Eligibility

| Track | Argument |
|---|---|
| **Digital Equity & Inclusivity** | Multilingual (5 Indian languages), offline, free, no data harvesting |
| **Health & Sciences** | Mental health is healthcare; evidence-based CBT techniques |
| **Safety & Trust** | Privacy-first architecture; never diagnoses; crisis escalation built-in |
| **Unsloth** | Fine-tuned Gemma 4 E2B using Unsloth on culturally-specific Indian data |

---

## ⚠️ Ethical Commitments

MentalBridge is built with explicit ethical guardrails:
- **Never diagnoses** any condition
- **Always recommends** professional help
- **Immediate crisis escalation** when self-harm language detected
- **Transparent** — never pretends to be human
- **Privacy by design** — zero data leaves the device

---

## 👤 Author

**Vishnu Prasad GS**
- HuggingFace: [vishnuprasadgs](https://huggingface.co/vishnuprasadgs)
- GitHub: [vishnu-prasad-g-s](https://github.com/vishnu-prasad-g-s)

---

*MentalBridge · Built for the Gemma 4 Good Hackathon 2026*
