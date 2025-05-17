import webbrowser
import requests
import pyttsx3
import pyjokes
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Hi, I am Iris, an AI assistant made by Dushyant")
speak("Hi, Iam Iris, How can I assist you today?")

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a6eebbd71f5d9aa48c163e534057ca12&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    des = data['weather'][0]['description']
    return f"It's {temp} degrees in {city} with {des}."

def news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=60a386e0c3e140659b23dd5156e82212"
    response = requests.get(url)
    news_data = response.json()
    headlines = news_data['articles']
    return headlines

def joke():
    return pyjokes.get_joke()

while True:
    command = input('What do you want me to do?\n').lower()

    if 'open youtube' in command or 'open yt' in command:
        webbrowser.open('https://youtube.com')
        speak('Opening YouTube')

    elif 'open netflix' in command:
        webbrowser.open('https://www.netflix.com')
        speak('Opening Netflix')

    elif 'time' in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        print("Current time is", current_time)
        speak("The time is " + current_time)

    elif 'weather' in command:
        city = input('Enter city name: ')
        weather_info = weather(city)
        print(weather_info)
        speak(weather_info)

    elif 'news' in command:
        headlines = news()
        print('Top 3 news headlines:')
        for i in range(3):
            print(f"{i + 1}. {headlines[i]['title']}")
            speak(headlines[i]['title'])

    elif 'joke' in command:
        j = joke()
        print(j)
        speak(j)

    elif 'bye' in command or 'exit' in command or 'quit' in command:
        print("Goodbye, hope you liked my project! ❤️")
        speak("Goodbye!")
        break

    else:
        print("Sorry, I can't do that yet 😥. But I can tell you WEATHER, NEWS, JOKE, and open YouTube or Netflix.")
        speak("Sorry, I can't do that yet.")
