---
language:
- en
- ta
- hi
- te
- kn
license: apache-2.0
base_model: unsloth/gemma-4-E2B-it
tags:
- mental-health
- india
- gemma4
- lora
- unsloth
- peft
- mental-health-india
- multilingual
datasets:
- custom
pipeline_tag: text-generation
---

# 🌉 MentalBridge — Gemma 4 E2B Fine-tuned for Indian Mental Health

**MentalBridge** is a fine-tuned version of [Gemma 4 E2B](https://huggingface.co/google/gemma-4-E2B-it) trained on culturally-calibrated Indian mental health conversations.

Built for the **Gemma 4 Good Hackathon 2026** · Unsloth Prize Track

---

## What makes this different from the base model

| Generic Gemma 4 Response | MentalBridge Response |
|---|---|
| "Here are 5 tips to manage stress: 1) Exercise 2) Sleep..." | "Carrying your mother's tears and your own dreams at the same time — that's an incredibly heavy place to be. What feels most suffocating about it right now?" |
| Gives American crisis numbers | Routes to iCall (9152987821) and Vandrevala Foundation |
| Western therapy language | Understands IIT pressure, CA failures, arranged marriage context |
| English only | Responds naturally in Tamil, Hindi, Telugu |

---

## Training Details

- **Base model**: `unsloth/gemma-4-E2B-it`
- **Method**: LoRA (Low-Rank Adaptation) via [Unsloth](https://github.com/unslothai/unsloth)
- **Platform**: Kaggle (2× Tesla T4 GPU)
- **Training time**: ~5 minutes
- **Dataset**: 192 examples (mental health intents + 14 custom Indian scenarios)
- **Final training loss**: 0.843
- **Epochs**: 3
- **LoRA rank**: r=16

### Training Config
```python
FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
)
```

---

## Dataset

### Sources
1. **Kaggle Mental Health Conversational Data** (elvis23/mental-health-conversational-data)
2. **Custom Indian scenarios** — hand-crafted for cultural relevance:

| Language | Example |
|---|---|
| English | "I failed my NEET exam and I can't face my parents." |
| Tamil | "நான் மிகவும் தனிமையாக உணர்கிறேன். என் குடும்பம் என்னை புரிந்துகொள்வதில்லை." |
| Hindi | "मुझे हर रात रोना आता है और मैं नहीं जानता क्यों।" |

### Topics covered
- NEET / CA / UPSC exam failure and family shame
- Arranged marriage pressure
- Job loss and financial shame
- Software engineer burnout (Indian IT culture)
- Family comparison and academic pressure
- Crisis detection → Indian helpline routing

---

## How to Use

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    "vishnuprasadgs/mentalbridge-gemma4-E2B-finetuned",
    max_seq_length=512,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

messages = [{"role": "user", "content": "I failed my CA exam for the third time. I can't face my parents."}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(input_ids=inputs, max_new_tokens=150, temperature=0.7)
print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

---

## System Prompt (used in MentalBridge app)

```
You are MentalBridge. Warm mental health first-aid companion for India.
Rules: Never say "I am AI". Match user language exactly. NO lists or bullets.
Max 3 short sentences. Indian helplines only: iCall 9152987821, Vandrevala 1860-2662-345.
If crisis: acknowledge pain first then mention iCall.
Structure: reflect → validate → one gentle question.
```

---

## Ethical Commitments

⚠️ **MentalBridge is NOT a therapist or diagnostic tool.**

- Never diagnoses any condition
- Always recommends professional help
- Immediate crisis escalation to Indian helplines
- Runs 100% on-device — zero data leaves the phone

---

## Application

This model powers the **MentalBridge** app — an offline-first mental health companion:
- GitHub: [YOUR_GITHUB_LINK]
- Built with Ollama for local inference

---

## Citation

```
@misc{mentalbridge2026,
  title={MentalBridge: Culturally-calibrated Mental Health AI for India},
  author={Vishnu Prasad GS},
  year={2026},
  note={Gemma 4 Good Hackathon submission}
}
```
