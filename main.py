#import openAI API
from typing import Self
import openai
import feedparser
from TTS.api import TTS

def load_KEY(keyfile):
    try:
        with open(keyfile, 'r') as f:
            api_key = f.readline().strip()
        return api_key

    except FileNotFoundError:
        print("Key file not found. Please make sure the file exists.")

    except Exception as e:
        print("An error occurred opening the API key file: ", e)



def fetchNews(entryIndex):
    NewsFeed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/US.xml")
    entry = NewsFeed.entires[entryIndex]

# tts_model = TTS.list_models(Self: TTS)[0]

# tts = TTS(tts_model)

wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])


openai.api_key = load_KEY("API_KEY")

# availableModels = openai.Model.list()



print("The following AI models are available via the API:filename")
print(availableModels)

output = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-16k',
    messages=[{"role":"user", "content": "In 5 words: Tell me about the US capitol."}]
)

print(output.choices[0].message.content)

#Get API key from file

#Get response from API

