import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import requests
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
  try:
     with sr.Microphone() as source:
        print('listening..')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bingo' in command:
            engine.say(command)
            print(command)
  except:
      pass
  return command
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        main_info = weather_data["weather"][0]["main"]
        temp = weather_data["main"]["temp"]
        return f"Currently in {city_name}, it's {main_info} with a temperature of {temp:.1f}°C."
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."

def run_bingo():
    command = take_command()
    if 'hello' in command:
        talk("Hello, i am bingo,how can i help you?")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        talk(f"The current time is {current_time}")
        print(current_time)

    elif 'play' in command:
        song = command.replace('play',"")
        talk('playing'+ song)
        pywhatkit.playonyt(song)


    elif 'search' in command:
        talk("What would you like me to search for?")
        search_query = take_command()
        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            talk(f"Here are the search results for {search_query}")

    elif 'weather' in command:
        talk("Sure, please tell me the city name.")
        city_name = take_command()
        api_key = "1f720509f2561055a4ffb294877497ea"
        weather_info = get_weather(city_name, api_key)
        talk(weather_info)

    elif 'are you single' in command:
        talk("no im not unlucky like you")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'exit' in command:
        talk("Goodbye!")
        exit()

if __name__ == "__main__":
    talk("Hello, I am your virtual assistant Bingo. How can I assist you today?")
    run_bingo()

