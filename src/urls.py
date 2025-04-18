import modules
from modules import *
def open_website(command):
    websites = {
        "open google": "https://www.google.com",
        "open youtube": "https://www.youtube.com",
        "open Reddit" : "https://www.reddit.com",
        "open facebook": "https://www.facebook.com",
        "open twitter": "https://www.twitter.com",
        "open chat GPT" : "https://www.chatgpt.com",
        "open background remover" : "https://remove.bg",
        "open wikipedia" : "https://www.wikipedia.org",
        "open python":"https://www.python.org",
        "open github": "https://github.com/Rustam-Singh-Bhadouriya"
    }

    # Convert the command to lowercase to make it case-insensitive
    command = command.lower()

    # Check if the command matches any website in the dictionary
    for site in websites:
        if site in command:
            print(f"Opening {site}...")
            webbrowser.open(websites[site])  # Open the site in the default browser
            return

    # If no match found, inform the user
    