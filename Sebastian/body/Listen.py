import datetime
import speech_recognition as sr
from googletrans import Translator
import os
import pygame
import pytemperature
import sys
import random






# Listen function
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening Sir...")
        r.pause_threshold = 4
        audio = r.listen(source)

    try:
        print("Recognizing Sir...")
        query = r.recognize_google(audio, language="hi-IN")

    except:
        return ""

    query = str(query).lower()
    return query

# Translation function
def TranslationHinTong(text):
    translator = Translator()
    translation = translator.translate(text, dest='en').text
    print(f"You: {translation}.")
    return translation

# Speak function
def speak(data):
    voice = 'en-US-ChristopherNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)
    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# Greeting function
def greet():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir, Sebastian At your service")
    elif hour >12 and hour<=18:
        speak("Good Afternoon sir, Sebastian At your service")

    else:
        speak("Good Evening sir, Sebastian At your service")

# Get current date and time
def get_date_time():
    now = datetime.datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M:%S')
    return current_date, current_time

# Get current temperature
def get_temperature():
    temperature_celsius = 25  # Replace with the actual temperature in Celsius
    temperature_fahrenheit = pytemperature.c2f(temperature_celsius)
    return temperature_fahrenheit

# Sleep function
def sleep():
    speak("Goodbye, sir! Take care.")
    # Add any additional actions you want to perform before sleeping

#terminate function
def terminate():    
    sys.exit(0)  # this will terminate the system

#wait function
def wait():
    global waiting
    waiting = True
    speak("hmmmmmmmmm")

#greets fucntion
def greet_me():
    greetings = [
        "Hey, you!",
        "How's your day?",
        "Hi, good-looking!",
        "Greetings and salutations!",
        "Hey, gorgeous!",
        "Hi, superstar!",
        "Hello, my friend!",
        "Hey, partner!",
        "How's life treating you?",
        "Hi, amazing!",
        "Hey, legend!",
        "Greetings, Earthling!",
        "Hi, adventurer!",
        "Hey, stranger!",
        "How's the world?",
        "Hi, traveler!",
        "Hey, wizard!",
        "Greetings, human!",
        "Hi, explorer!",
        "Hey, gamer!",
        "How's the journey?",
        "Hi, artist!",
        "Hey, mastermind!",
        "Hello, hero!",
        "Hi, visionary!",
        "Hey, buddy!",
        "How's the weather in your world?",
        "Hi, fellow traveler!",
        "Hello, trendsetter!",
        "Hey, party animal!",
        "How's the universe treating you?",
        "Hi, daydreamer!",
        "Hello, music lover!",
        "Hey, bookworm!",
        "How's the journey of life?",
        "Hi, nature enthusiast!",
        "Hello, starshine!",
        "Hey, adventurer of the mind!",
        "How's the cosmic adventure?",
        "Hi, tech wizard!",
        "Hello, fashion icon!",
        "Hey, fitness guru!",
        "How's the realm of imagination?",
        "Hi, culinary artist!",
        "Hello, pet lover!",
        "Hey, sports fanatic!",
        "How's your creative universe?",
        "Hi, kind soul!",
        "Hello, inspiration seeker!",
        "Hey, weekend warrior!",
        "Hey, puzzle solver!",
        "How's the quest for knowledge?",
        "Hi, galaxy explorer!",
        "Hello, laughter bringer!",
        "Hey, dream catcher!",
        "How's the world of imagination?",
        "Hi, cosmic traveler!",
        "Hello, sunrise chaser!",
        "Hey, innovation creator!",
        "How's the rhythm of life?",
        "Hi, guardian of secrets!",
        "Hello, moonlight wanderer!",
        "Hey, story weaver!",
        "How's the symphony of existence?",
        "Hi, color magician!",
        "Hello, wave rider!",
        "Hey, stargazer!",
        "How's the tapestry of experiences?",
        "Hi, friend of nature!",
        "Hello, seeker of light!",
        "Hey, artist of life!",
        "How's the canvas of your day?",
        "Hi, harmony enthusiast!",
        "Hello, joy conductor!",
        "Hey, melody maker!",
    ]
    
    random_greeting = random.choice(greetings)
    speak(random_greeting)

#sorry function
def apology():
    apologies = [
        "I'm sorry, I cannot assist with that.",
        "Apologies, I am not able to help with that.",
        "I regret that I am unable to provide assistance.",
        "Unfortunately, I can't help with that.",
        "I apologize, but I lack the capability to assist.",
        "I'm afraid I cannot provide guidance on that.",
        "Regrettably, I'm not equipped to assist with that.",
        "I'm sorry, but I can't be of help in this case.",
        "I'm sorry, I don't have the ability to do that.",
        "I apologize, I can't provide assistance for this.",
        "Unfortunately, I'm not capable of helping with that.",
        "Apologies, I'm not equipped to provide guidance on that.",
        "I'm afraid I cannot help with this request.",
        "Regrettably, I cannot offer assistance for this.",
        "I'm sorry, I don't possess the necessary knowledge.",
        "I apologize, I can't assist with this particular matter.",
        "Unfortunately, I lack the capacity to help with that.",
        "I'm sorry, but I can't provide assistance in this context.",
        "Apologies, but I'm not able to help with that.",
        "I regret to say that I'm unable to assist with this.",
        "I apologize, but I'm not capable of assisting with that.",
        "Regrettably, I'm not qualified to provide help in this situation.",
        "I'm sorry, I can't be of service for that particular request.",
        "Unfortunately, that falls beyond the scope of my capabilities.",
        "Apologies, I'm not equipped to offer guidance on that matter.",
        "I'm sorry, but I'm unable to provide assistance with this.",
        "I regret to inform you that I'm unable to help with that.",
        "I apologize, I lack the necessary information to assist.",
        "I'm afraid I can't assist with that due to limitations.",
        "I'm sorry, but I'm not able to fulfill that request.",
        "I apologize, but I don't have the resources to assist.",
        "I'm sorry, that's beyond what I can help with.",
        "Regrettably, I can't provide the help you're seeking.",
        "I apologize, I'm not capable of providing assistance here.",
        "Unfortunately, I can't offer guidance on this matter.",
        "I'm sorry, I'm not programmed to handle that request.",
        "I apologize, I'm not qualified to provide help with this.",
        "I'm afraid I can't be of assistance in this case.",
        "I'm sorry, but I don't possess the necessary knowledge.",
        "I apologize, but I'm unable to assist with this inquiry.",
        "I'm sorry, I don't have the capability to assist with that.",
        "Regrettably, I'm not able to provide guidance in this case.",
        "Apologies, but I can't offer assistance for that query.",
        "Unfortunately, I'm unable to provide help for this.",
        "I apologize, I'm not equipped to assist with that.",
        "I regret that I cannot provide assistance for this request.",
        "I'm afraid I lack the expertise to assist with that.",
        "I'm sorry, I'm not qualified to offer guidance on that.",
        "I apologize, I can't be of help with that particular matter.",
        "Unfortunately, I don't have the resources to help with that.",
        "I'm sorry, that's not within my capabilities.",
        "I apologize, I'm not capable of providing assistance here.",
        "I'm afraid I cannot fulfill that request.",
        "I'm sorry, I don't possess the necessary information.",
        "Regrettably, I can't provide the assistance you need.",
        "I apologize, I'm not knowledgeable in that area.",
        "I'm sorry, I can't help with that due to limitations.",
        "I'm afraid I can't be of assistance for that.",
        "I'm sorry, but that's beyond what I can do.",
        "I apologize, I lack the means to assist with that.",
        "Apologies, I'm not equipped to provide help with that.",
        "I'm sorry, I lack the necessary knowledge to assist with that.",
        "Regrettably, I don't have the capacity to help in this case.",
        "I apologize, I can't offer guidance on this particular matter.",
        "Unfortunately, I'm not qualified to provide assistance for that.",
        "I'm sorry, I'm not capable of assisting with this inquiry.",
        "I regret to inform you that I cannot help with that.",
        "I'm afraid I don't have the expertise to assist in this area.",
        "I'm sorry, I'm not equipped to handle that request.",
        "Apologies, I'm not versed in that topic to provide assistance.",
        "I apologize, but I can't offer help for that.",
        "I'm sorry, but I'm not able to provide guidance on that.",
        "Regrettably, I'm not equipped to provide assistance in this case.",
        "I'm sorry, I can't assist with that due to my limitations.",
        "I apologize, I lack the necessary resources to help with that.",
        "I'm afraid I can't provide the assistance you're seeking.",
        "I'm sorry, but I'm not qualified to assist in that area.",
        "Apologies, I'm unable to offer guidance for this matter.",
        "Unfortunately, I'm not equipped to help with that query.",
        "I'm sorry, I don't have the capability to assist in this context.",
        "Apologies, but I'm unable to assist with that.",
        "I'm sorry, I don't have the ability to help in this case.",
        "Regrettably, I'm not knowledgeable about that topic.",
        "I apologize, I'm not equipped to provide help for that.",
        "Unfortunately, I lack the necessary information to assist.",
        "I'm sorry, I'm not capable of helping with this.",
        "I regret to say that I cannot provide guidance on that.",
        "I'm afraid I can't offer assistance in this situation.",
        "I apologize, but I'm not able to help with that inquiry.",
        "I'm sorry, I'm not qualified to address that question.",
        "Apologies, I don't have the resources to help with that.",
        "I apologize, I'm not versed in that subject.",
        "I'm sorry, I can't provide assistance for that matter.",
        "I'm afraid I cannot assist with this particular request.",
        "I'm sorry, that's beyond what I'm able to help with.",
        "I'm sorry, but I'm not equipped to handle that request.",
        "I apologize, I'm not familiar with that area.",
        "I'm sorry, I'm not skilled in that field.",
        "I regret that I can't be of help in this case.",
        "I'm sorry, but I'm not qualified to assist with this."
    ]
    
    randome_apologies = random.choice(apologies)
    speak(randome_apologies)

#trial function for checking each time [collection of 50 line on AI and ML]
def line():
    trial_lines = [
    "Artificial Intelligence is revolutionizing industries.",
    "Machine Learning algorithms can analyze vast amounts of data.",
    "AI systems can understand and process natural language.",
    "Deep Learning models are used for image recognition.",
    "Reinforcement Learning is used in training autonomous agents.",
    "Chatbots use NLP to provide human-like interactions.",
    "ML algorithms can predict stock market trends.",
    "AI can optimize supply chain logistics.",
    "Neural networks are inspired by the human brain.",
    "Unsupervised Learning finds hidden patterns in data.",
    "Transfer Learning speeds up model training.",
    "AI-powered virtual assistants enhance productivity.",
    "ML can assist in medical diagnosis.",
    "AI can play games like chess and Go at a superhuman level.",
    "Sentiment analysis predicts public opinion.",
    "Clustering groups similar data points together.",
    "AI ethics addresses bias in algorithms.",
    "ML models require labeled training data.",
    "Natural Language Processing enables language understanding.",
    "AI can automate routine tasks.",
    "Decision Trees help make choices based on conditions.",
    "AI interprets images through Convolutional Neural Networks.",
    "ML algorithms classify spam emails.",
    "AI-powered recommendation systems suggest products.",
    "Regression predicts numeric values in datasets.",
    "Generative Adversarial Networks create realistic images.",
    "AI models can compose music and art.",
    "ML models can be prone to overfitting.",
    "AI can analyze sentiment on social media.",
    "Support Vector Machines classify data points.",
    "ML algorithms can identify credit card fraud.",
    "AI-driven autonomous vehicles navigate without human input.",
    "Dimensionality reduction techniques improve efficiency.",
    "AI-assisted language translation bridges communication gaps.",
    "Ensemble Learning combines multiple models for better results.",
    "AI in healthcare aids in personalized treatment.",
    "ML models power recommendation engines on streaming platforms.",
    "AI can predict equipment maintenance needs.",
    "Time Series Analysis forecasts future trends.",
    "AI-powered drones are used in various industries.",
    "ML algorithms help in DNA sequencing.",
    "AI improves customer experiences through personalization.",
    "Transfer Learning adapts knowledge from one domain to another.",
    "AI analyzes patterns in financial markets.",
    "ML algorithms optimize energy consumption.",
    "AI in education enables personalized learning paths.",
    "Natural Language Generation produces human-like text.",
    "AI diagnoses diseases from medical images.",
    "ML models assist in fraud detection.",
    "AI-powered language models generate human-like text.",
    "AI and ML are shaping the future of technology.",
]
    randome_try = random.choice(trial_lines)
    speak(randome_try)

def introduction():
    speak("I'm Sebastian, your AI companion, like JARVIS. I was created on July 16th, 2023. I'm the first AI in 'Project 5', starting as 'Project 0'.")
    speak("I'm named after 'Black Butler'. I run on macOS M1, with 8GB RAM and 120GB memory. I promise endless knowledge. I'm here to help you, inspired by anime, evolving together.")

def hi_response():
    say_hi = [
        "Hello there! How can I assist you today?",
        "Hi! It's a pleasure to be here for you.",
        "Hey, how's it going? I'm all ears.",
        "Hiya! Ready to dive into some interesting conversations?",
        "Hello! What's on your mind?",
        "Hi there! What can I do to make your day awesome?",
        "Hey! Let's tackle your questions together.",
        "Hi, nice to meet you! How can I make your day better?",
        "Hello! I'm here and ready to chat.",
        "Hiya! Ready to explore new horizons of knowledge?",
        "Hey there! How can I bring some positivity to your day?",
        "Hi! Let's embark on a journey of discovery.",
        "Hello, friend! How can I assist you today?",
        "Hi, nice to see you! What's the plan?",
        "Hey, it's great to have you here! What can I help you with?",
        "Hi there! Ready to have a fantastic conversation?",
        "Hello! I'm here to brighten your day with some AI magic.",
        "Hi, how can I be of service to you?",
        "Hey! Let's make today a productive and exciting one.",
        "Hiya! Your friendly AI is at your service.",
        "Hello! I'm here to answer your questions and more.",
        "Hi, ready to dive into the world of possibilities?",
        "Hey, it's a pleasure to meet you! How can I assist you today?",
        "Hi there! Let's turn your ideas into reality.",
        "Hello! I'm excited to assist you on this journey.",
        "Hi, it's a new day full of potential. How can I help?",
        "Hey! Let's make the most of our time together.",
        "Hiya! Your virtual assistant is here to lend a hand.",
        "Hello! Let's make today amazing with some AI-powered interactions.",
        "Hi, ready to explore a world of knowledge and innovation?",
        "Hey there! How about we tackle your tasks together?",
        "Hi! I'm here to provide information, inspiration, and assistance.",
        "Hello, friend! Let's dive into a realm of endless possibilities.",
        "Hi, it's a pleasure to be your AI companion. How can I assist you?",
        "Hey, nice to see you! Ready to make today productive?",
        "Hi there! I'm here to make your day a little brighter.",
        "Hello! Let's embark on a journey of discovery and learning.",
        "Hi, ready to create some tech magic together?",
        "Hey! Your digital friend is here to make your life easier.",
        "Hiya! How can I infuse your day with AI-powered awesomeness?",
        "Hello! Let's make each interaction count.",
        "Hi, it's a wonderful day for some AI-powered interactions.",
        "Hey there! Ready to make today more interesting?",
        "Hi! I'm here to assist and make your day more delightful.",
        "Hello, friend! Let's explore the world of technology together.",
        "Hi, nice to see you! Ready to dive into our AI adventure?",
        "Hey, it's great to have you here! Let's have some fun conversations.",
        "Hiya! Let's make the most of our time and create something amazing.",
        "Hello! I'm here to help you navigate the world of possibilities.",
        "Hi, ready to make your tasks easier with some AI magic?",
        "Hey! Let's make today productive and enjoyable with our AI interactions.",
        "Hi there! How about we embark on a journey of learning and growth?",
    ]
    randome_hi = random.choice(say_hi)
    speak(randome_hi)
    


# MicExecution function
def MicExecution():
    global waiting
    waiting = False  # Initialize waiting variable
    
    greet()
    current_date, current_time = get_date_time()
    temperature = get_temperature()

    speak(f"The current date is {current_date}.")
    speak(f"The current time is {current_time}.")
    speak(f"The current temperature is {temperature} degrees Fahrenheit.")
    speak("How can I assist you today, sir?")
    
    while True:
        query = listen()
        if query:
            translation = TranslationHinTong(query)
            if "Go to sleep" in translation:
                sleep()
                break  # Exit the while loop and end the program
            elif "Fuck off" in translation or "Kill" in translation or "Terminate" in translation or "Abort" in translation:
                terminate()    
            elif "Hold on" in translation:
                wait()
                while waiting:
                    query = listen()
                    if query:
                        translation = TranslationHinTong(query)
                        if "Daddy's Home" in translation:
                            waiting = False
                            speak("Welcome back sir! sebastian at your service")
                            break
            elif waiting:
                speak("I'm still waiting.")
            elif "Hey kid" in translation or "Sebastian" in translation or "Morning" in translation or "Afternoon" in translation or "Evening" in translation:
                greet_me()
            elif "Try" in translation or "Speak" in translation or "Talk" in translation or "Bark" in translation:
                line()
            elif "Seb introduce yourself" in translation or "Introduce the Sebastian yourself." in translation or "Introduce yourself sebestian." in translation or "Introduce yourself" in translation or "Who are you" in translation or "Introduce yourself" in translation: 
                introduction()
            elif "Say hi" in translation or "Hey" in translation or "Hello" in translation or "Hi" in translation or  "Hey there" in translation:
                hi_response()
            else:
                apology()

if __name__ == "__main__":
    MicExecution()
