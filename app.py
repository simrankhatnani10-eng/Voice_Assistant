import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
  
# Dictionary of Indian states and capitals
state_capitals = {
    "andra pradesh":"Amaravati",
    "maharashtra":"Mumbai",
    "karnataka":"Bengaluru",
    "tamil nadu":"Chennai",
    "west bengal":"Kolkata",
    "uttar pradesh":"Lucknow"
}

st.title("State capital voice assistant")

def speak(text):
    gtts = gTTS(text = text,lang = "en")
    filename = "State_Capital.mp3"
    gtts.save(filename)
    os.system(f"start{filename}")
    
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("say the name of an indian state..")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        state = recognizer.recognize_google(audio)
        state = state.lower() 
        print("You said:",state)
        return state
    except:
        return None
    
    
# Main 
state_name = listen() 

if state_name:
    if state_name in state_capitals:
        capital = state_capitals[state_name]
        answer = f"The capital of {state_name} is {capital}"
        
    else:
        answer = "Sorry , I dont have that state in my database."
    
else:
    answer = "Sorry,I could not understand."
    
    
print(answer)
speak(answer)                
        


    