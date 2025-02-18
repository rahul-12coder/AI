# import pyttsx3
# import speech_recognition as sr
# import introduction as intro
# import daytime
# import pyautogui
# import wikipedia
# import webbrowser
# import geminiApiRequest as ai
# import mtranslate
# import pyjokes
# import os
# import pyaudio
# import user_config
# import datetime



# engine=pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')       
# engine.setProperty('voice', voices[0].id) 
# engine.setProperty('rate', 180) 


# User = user_config.user
# Assistant = user_config.Assistant


# def speak(audio):
#     mtranslate.translate(audio, to_language="en-in", from_language="en-in")
#     engine.say(audio)
#     engine.runAndWait()


# def greetMe():
#     hour = datetime.datetime.now().hour
#     if (hour >= 6) and (hour < 12):
#         speak(f"Good Morning{User}")
#     elif (hour >= 12) and (hour < 16):
#         speak(f"Good AfterNoon{User}")
#     elif (hour >= 16) and (hour < 19):
#         speak(f"Good Night{User}")
#     speak(f"I am {Assistant} how can i help you sir")

# def command():
#     content = " "
#     while content == " ":
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#                 print("Say something.........")
#                 r.pause_threshold = 1
#                 audio=r.listen(source)
                
#         try:
#             content = r.recognize_google(audio, language='en-in')
#           #   print("You said............. "+ content)
#             content = mtranslate.translate(content,to_language="en-in")
#           #   print("You said............. "+ content)
#         except Exception as e:
#             print("Please Try Again...")
#             speak("Please Try Again...")
#         return content
# def time():
#      now_time = daytime.datetime.datetime.now().strftime("%H:%M")
#      print(now_time)
#      speak(" Sir, current time is "+ str(now_time))
# def date():
#     now_date = daytime.datetime.datetime.now().strftime("%d:%m")
#     print(now_date)
#     speak("Sir, current date is "+ str(now_date))


# def screenshot(FileName,PathToSave):
#     path1name = FileName + ".png"
#     path1 = str(PathToSave) + path1name
#     AA = pyautogui.screenshot()
#     AA.save(path1)
#     os.startfile(path1)


# def main_process():
#      jarvis_chat=[]

#      while True:
#         request = command().lower()
#         print(request)
#         if "who are you" in request:
#           print("Hello Sir , I Am Jarvis .")
#           print("Your Personal AI Assistant!")
#           print("How May I Help You?")
#           speak("Hello Sir , I Am Jarvis .")
#           speak("Your Personal AI Assistant!")
#         #   speak("How May I Help You?")


#      #    elif "hi jarvis" in request:
#      #         print(intro.hiijarvis)
#      #         speak(intro.hiijarvis)


#         elif 'how r u' in request:
#             print("I Am Fine Sir!")
#             print("Whats About YOU?")
#             speak("I Am Fine Sir!")
#             speak("Whats About YOU?")

#         elif 'you need a break' in request:
#             print("Ok Sir , You Can Call Me Anytime !")
#             print("Just Say Wake Up Jarvis!")
#             speak("Ok Sir , You Can Call Me Anytime !")
#             speak("Just Say Wake Up Jarvis!")
#             break
        
#         elif "say time" in request:
#              time()

#         elif "say date" in request:
#              date()
        
#         elif "open youtube" in request:
#              speak("Loading...., Sir")  
#              webbrowser.open("www.youtube.com")
             

#         elif "open" in request:
#              speak("Loading..., sir")  
#              query = request.replace("open","")
#              pyautogui.press("super")
#              pyautogui.typewrite(query)
#              pyautogui.sleep(2)
#              pyautogui.press("enter")
       

#         elif " search wikipedia " in request:
#              speak("Loading..., sir")  
#              request = request.replace("jarvis","")
#              request = request.replace("search wikipedia","")
#              print(request)
#              result = wikipedia.summary(request, sentences = 2)
#              print(result)
#              speak(result)

#         elif "jarvis search from google" in request:
#              speak("Ofcourse, sir Wait a second")
#              request = request.replace("jarvis search from google","")
#              request = request.replace("search","")
#              print(request)
#              webbrowser.open("https://www.google.com/search?q="+request)

#      #    elif "take Screenshot" in request:
#      #         screen_shot()


#         elif 'remember that' in request:
#             remeberMsg = request.replace("remember that","")
#             remeberMsg = remeberMsg.replace("jarvis","")
#             speak("You Tell Me To Remind You That :"+remeberMsg)
#             remeber = open('data.txt','w')
#             remeber.write(remeberMsg)
#             remeber.close()

#         elif 'what do you remember' in request:
#             remeber = open('data.txt','r')
#             speak("You Tell Me That" + remeber.read())

#         elif 'repeat my word' in request:
#             jj = request.replace("repeat my word","")
#             jj = request.replace("Jarvis","")
#             speak(f"You Said : {jj}")

#         elif 'joke' in request:
#             get = pyjokes.get_joke()
#             print(get)
#             speak(get)


#         elif "good night" "good morning" "good afternoon" in request:
#             greetMe()

#         else:
#              speak("Sir, Here Are Your Answer")
#              request = request.replace("jarvis","")

#              print(request)
#              jarvis_chat.append(request)
#              response = ai.send_request2(jarvis_chat)

#              print(response)
#              jarvis_chat.append(response)
#              speak(response)
             
             
             

# main_process()

# if __name__ == '__main__':
#     greetMe()





from Backend.Model import FirstLayer
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values
from asyncio import run
from time import sleep
import subprocess
import threading
import json
import os



env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
DeafaultMessage = f"""{Username} : Hello {Assistantname}, How are you?
{Assistantname} : Welcome {Username}. I am doing well. How may i help you?"""
subprocesses = []
Functions = ["open", "close", "play", "system", "content", "google search", "youtube search"]

def ReadChatlogjson():
    with open(r"Data\Chatlog.json", "r", encoding='utf-8') as file:
        chatlog_data = json.load(file)
    return chatlog_data

def ChatLogIntegration():
    json_data = ReadChatlogjson()
    formatted_chatlog = ""
    for entry in json_data:
        if entry["role"] == "user":
            formatted_chatlog += f"User: {entry['content']}\n"
        elif entry["role"] == "assistant":
            formatted_chatlog += f"Assistant: {entry['content']}\n"
    formatted_chatlog = formatted_chatlog.replace("user", Username + " ")
    formatted_chatlog = formatted_chatlog.replace("Assistant", Assistantname + " ")

    with open(('Database.data'), "w", encoding='utf-8') as file:
        file.write((formatted_chatlog))


def MainExecution():

    TaskExecution = False
    # ImageExecution = False
    # ImageGenerationQuery = ""

    print("Listenning.....")
    Query = SpeechRecognition()
    print(f"{Username} : {Query}")
    print("Thinking...")
    Decision = FirstLayer(Query)

    print("")
    print(f"Desicion : {Decision}")
    print("")

    G = any([i for i in Decision if i.startswith("general")])
    R = any([i for i in Decision if i.startswith("realtime")])

    Mearged_query =  " and ".join(
        [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
    )

    for queries in Decision:
        if TaskExecution == False:
            if any(queries.startswith(func) for func in Functions):
                run(Automation(list(Decision)))
                TaskExecution = True


    if G and R or R:
        
        print("Searching....")
        Answer = RealtimeSearchEngine((Mearged_query))
        print("Answering....")
        TextToSpeech(Answer)
        return True
    
    else:

        for Queries in Decision:

            if "general" in Decision:
                print("Thinking....")
                QueryFinal = Queries.replace("general", "")
                Answer = ChatBot((QueryFinal))
                print(f"{Assistantname} : {Answer}")
                TextToSpeech(Answer)
                return True
            
            elif "realtime" in Queries:
                print("searching......")
                QueryFinal = Queries.replace("realtime", "")
                Answer = RealtimeSearchEngine((QueryFinal))
                print(f"{Assistantname} : {Answer}")
                print("Answering......")
                TextToSpeech(Answer)
                return True
            
            elif "exit" in Queries:
                QueryFinal = "Okay, Bye!"
                Answer = ChatBot((QueryFinal))
                print(f"{Assistantname} : {Answer}")
                print("Answering....")
                TextToSpeech(Answer)
                print("Answering....")
