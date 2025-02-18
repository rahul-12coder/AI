import pygame
import random
import asyncio
import edge_tts
import os 
from dotenv import dotenv_values


env_vars = dotenv_values(".env")
AssistantVoices = env_vars.get("AssistantVoices")


async def TextToAudioFile(text) -> None:
    file_path = r"Data\speech.mp3"

    if os.path.exists(file_path):
        os.remove(file_path)


    communicate = edge_tts.Communicate(text,AssistantVoices, pitch='+5Hz', rate='+13%')
    await communicate.save(r"Data\speech.mp3")


def TTS(Text, func=lambda r=None: True):
    while True:
        try:

            asyncio.run(TextToAudioFile(Text))

            pygame.mixer.init()

            pygame.mixer.music.load(r"Data\speech.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if func() == False:
                    break
                pygame.time.Clock().tick(10)
            return True
        
        except Exception as e:
            print(f"Error in TTS: {e}")

        finally:
            try:
                func(False)
                pygame.mixer.music.stop()
                pygame.mixer.quit()

            except Exception as e:
                print(f"Error in finally block: {e}")


def TextToSpeech(Text, func=lambda r=None: True):
    Data = str(Text).split(".")

    responses = [
        'The rest of the result has been printed to the chat screen, kindly check it out.',
        'You can see the rest of the text on the chat screen.',
        'The remaining part of the text is now on the chat screen.',
        "You'll find more text on the chat screen.",
        'Please check the chat screen for additional text.'
    ]

    if len(Data) > 4 and len(Text) >= 2500:
        TTS(" ".join(Text.split(".")[0:2]) + ", " + random.choice(responses), func)

    else:
        TTS(Text, func)

if __name__ == "__main__":
    while True:
        TextToSpeech(input("Enter The Text: "))
    