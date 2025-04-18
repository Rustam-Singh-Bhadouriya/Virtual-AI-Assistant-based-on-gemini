import modules
from modules import *
import urls
from urls import *

os.system("pip install SpeechRecognition pyttsx3 pyaudio gtts langdetect google-api-python-client google-generativeai")

# Initialize API Key and configuration
api = modules.api_key

# Function to start the chat and get response from Gemini
def get_gemini_response(prompt):
    genai.configure(api_key=api)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Please reply in not more than 30 words.\n{prompt}")
    return response.text

# Function to recognize speech input
def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak something...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio)
        print(f"🗣️ You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand the audio.")
        speak_response("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("⚠️ Could not request results from Google.")
        return None

# Function to speak the response from Gemini
def speak_response(response_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech speed
    
    # Get available voices and set one
    voices = engine.getProperty('voices')
    if len(voices) > 1:  # Check if there are multiple voices available
        engine.setProperty('voice', voices[1].id)  # Typically index 1 is female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Default voice if only one available
    
    # Speak the response
    engine.say(response_text)
    engine.runAndWait()

while True:
    # Get speech input from the user
    prompt = recognize_speech()
    
    if prompt:  # If speech input was recognized
        # Check if the command is to open a website
        open_website(prompt)
        if prompt == "good bye".lower():
            break
        else:

        # Get response from Gemini based on prompt (optional step, only if not opening a website)
            response_text = get_gemini_response(prompt)
            print(f"🤖 Gemini says: {response_text}")
            
            # Speak the Gemini response
            speak_response(response_text)


speak_response("Bye Have a Nice Day") # End point of program
