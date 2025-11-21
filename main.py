import speech_recognition as sr
import webbrowser
import pyttsx3
import os
from gtts import gTTS
from musicLibrary import music
import datetime
import requests
import openai  

# OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speaks(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    os.system("start temp.mp3")

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=200,
            temperature=0.7,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Error talking to OpenAI: {str(e)}"

def process_command(command):
    """Process the actual command after wake word is detected"""
    
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open chat gpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("play"):
        song = command.split("play")[-1].strip().lower()
        if song in music:
            link = music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Searching {song} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")

    elif "ask ai" in command or "question" in command:
        speak("What would you like to ask?")
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=10)
                question = recognizer.recognize_google(audio)
                print(f"You asked: {question}")
                answer = ask_openai(question)
                print(f"AI Answer: {answer}")
                speak(answer)
            except Exception as e:
                speak("Sorry I couldn't catch that")
                print(f"Error: {e}")

    elif "exit" in command or "goodbye" in command:
        speak("Goodbye")
        return False
    
    else:
        speak("I didn't understand that command. Please try again.")
    
    return True

# === Main Program ===
if __name__ == "__main__":
    speak("Initializing Case...")
    
    while True:
        with sr.Microphone() as source:
            print("Listening for wake word 'Case'...")
            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                
                # Check if wake word is detected
                if "case" in command:
                    speak("Yes, I'm listening. How can I help you?")
                    
                    # Now listen for the actual command
                    with sr.Microphone() as source2:
                        try:
                            print("Listening for command...")
                            recognizer.adjust_for_ambient_noise(source2, duration=0.5)
                            audio2 = recognizer.listen(source2, timeout=10)
                            actual_command = recognizer.recognize_google(audio2).lower()
                            print(f"Command: {actual_command}")
                            
                            # Process the command
                            continue_running = process_command(actual_command)
                            if not continue_running:
                                break
                                
                        except sr.UnknownValueError:
                            speak("Sorry, I couldn't understand that.")
                        except sr.RequestError as e:
                            speak("There was an error with the speech recognition service.")
                            print(f"Recognition error: {e}")
                        except sr.WaitTimeoutError:
                            speak("I didn't hear anything. Please try again.")
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Recognition error: {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out.")