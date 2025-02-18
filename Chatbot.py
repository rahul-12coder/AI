from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistant = env_vars.get("Assistantname")
# GorqAPIKey = env_vars.get("GrogAPIKey")

GorqAPIKey =

client = Groq(api_key=GorqAPIKey)


messages = []

System = (
    f"Hello, I am {Username}, you are a very accurate and advanced AI chatbot named {Assistant} "
    f"which also has real-time up-to-date information from the internet.\n"
    "*** Do not tell time unless I ask, do not talk too much, just answer the question. ***\n"
    "*** Provide answers in a professional way. Make sure to use proper grammar with full stops, commas, and question marks. ***\n"
    "*** Reply in the same language as the question: Hindi in Hindi, English in English. ***\n"
    "*** Do not mention your training data or provide notes in the output. Just answer the question. ***"
)



SystemChatBot = [
    {"role": "system", "content": System}
]


try:
    with open(r"Data\Chatlog.json", "r") as f:
        messages = load(f)

except FileNotFoundError:
    with open(r"Data\Chatlog.json", "w") as f:
        dump([],f)




def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")


    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate:{date}\nMonth:{month}\nYear:{year}\n"
    data += f"Time:{hour} hours :{minute} minutes :{second}\n"

    return data


def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)



def ChatBot(Query):

    try:
        with open(r"Data\Chatlog.json", "r") as f:
            messages = load(f)
        
        messages.append({"role": "user", "content": f"{Query}"})


        completion = client.chat.completions.create(

                model ="llama-3.3-70b-versatile",
                messages = SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
                max_tokens=1024,
                temperature = 1,
                top_p=1,
                stream = True,
                stop = None
        )
        


        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content


        Answer = Answer.replace("</s>", "")


        messages.append({"role": "assistant", "content": Answer})


        with open(r"Data\Chatlog.json","w") as f:
            dump(messages,f, indent=4)

        return AnswerModifier(Answer=Answer)
    

    except Exception as e:
        print(f"Error : {e}")
        
        with open(r"Data\chatlog.json","w") as f:
            dump([],f, indent=4)
        return ChatBot(Query)
    

if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question : ")
        print(ChatBot(user_input))
