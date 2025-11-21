# Case-  AI  Voice Assistant

## Overview
Case is an **AI voice assistant** developed in Python.
It is able to:
- Open websites (Google, YouTube, ChatGPT, etc.)
- Play music from a local library or search on YouTube
- Respond to questions using **OpenAI GPT-3.5**
- Say answers using **text-to-speech**
- Do simple tasks such as tell the time, date, or recall notes

---

## Features
- Wake word recognition ("Case")
- Voice commands through **speech recognition**
- Dual support for `pyttsx3` and `gTTS` text-to-speech  - Music library with automatic YouTube search fallback  - Q&A using AI-based OpenAI GPT-3.5  - Optional: Google AI Studio (Gemini) support  - Optional: Memory module to retain user notes  - Optional: Date/time/weather functions

---
## Usage
    Say “Case” to wake the assistant
    Give commands like:
    “Open Google”
    “Open YouTube”
    “Play [song_name]song”
    “Ask AI [your question]”
    “What time is it?”
    "What Date is it?"
    To exit, say “Goodbye” or “Exit”

## Dependencies

    Python 3.9+
    speechrecognition
    pyttsx3
    gtts
    openai
    webbrowser (built-in)
    google-generativeai (for Google AI)

    ---