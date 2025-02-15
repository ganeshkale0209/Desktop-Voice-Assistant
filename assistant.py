import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import tkinter as tk

print('I am your desktop assistant.')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning, ganesh sir")
        print("Hello, Good Morning, ganesh sir")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon, ganesh sir")
        print("Hello, Good Afternoon, ganesh sir")
    else:
        speak("Hello, Good Evening, ganesh sir")
        print("Hello, Good Evening, ganesh sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def login_window():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Login")

    tk.Label(root, text="Username:").grid(row=0, column=0)
    tk.Label(root, text="Password:").grid(row=1, column=0)

    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "admin123":
            root.destroy()
            main_program()
        else:
            speak("Invalid username or password")

    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)

    root.mainloop()

def main_program():
    speak("I am your desktop assistant.")
    wishMe()

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "bye" in statement or "stop" in statement or "thank you" in statement:
            speak('I am happy to help you sir. Call me anytime if you need me.')
            print('I am happy to help you sir. Call me anytime if you need me.')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature in Kelvin unit is " +
                      str(current_temperature) +
                      "\nHumidity in percentage is " +
                      str(current_humidity) +
                      "\nDescription: " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("City Not Found")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am a desktop assistant and also personal assistant. I am programmed to perform minor tasks like '
                  'opening YouTube, Google Chrome, Gmail, and Stack Overflow. I can predict time, take a photo, '
                  'search Wikipedia, predict weather in different cities, get top headline news from Times of India, '
                  'and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Ganesh kale")
            print("I was built by Ganesh kale")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is Stack Overflow")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India. Happy reading!')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your PC will log off in 10 seconds. Make sure you exit from all applications.")
            subprocess.call(["shutdown", "/l"])

        time.sleep(3)

if __name__ == '__main__':
    login_window()
