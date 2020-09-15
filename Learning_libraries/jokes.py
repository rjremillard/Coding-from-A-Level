import pyttsx3
import requests

# init
engine = pyttsx3.init()

# code
response = requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
json_ = response.json()

engine.say(text=json_["setup"])
engine.say(text=json_["punchline"])

# run
engine.runAndWait()
engine.stop()
