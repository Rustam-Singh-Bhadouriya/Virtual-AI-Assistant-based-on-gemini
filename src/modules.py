import speech_recognition  as sr
import pyttsx3
import pyaudio
import base64
import os
from google import genai
from google.genai import types
import json
import google.generativeai as genai
import threading
from gtts import gTTS
from langdetect import detect
import webbrowser 

with open("keys.json") as codes:
    api = json.load(codes)

api_key = api['API']