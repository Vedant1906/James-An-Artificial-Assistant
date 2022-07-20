#initialise SAPI5
Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()
