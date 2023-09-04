from typing import Self
import openai
import feedparser
from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
from google.cloud import texttospeech

nytRSS = "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"
hackadayRSS = "https://hackaday.com/blog/feed/"
arsTechnicaRSS = "https://feeds.arstechnica.com/arstechnica/index"

def googleTTS(inputText, outputFile):
    client = texttospeech.TextToSpeechClient()
    synthInput = texttospeech.SynthesisInput(text=inputText)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        name="en-US-Neural2-I",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE

    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input = synthInput, voice=voice, audio_config=audio_config
    )

    with open(outputFile, "wb") as out:
        out.write(response.audio_content)


def getStringDate():
    current_date = datetime.now()
    day = current_date.day
    month = current_date.strftime('%B')
    year = current_date.strftime('%Y')
    # Determine the suffix for the day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    # Construct the date string
    date_string = f"{month} {day}{suffix} {year}"
    return date_string

def load_KEY(keyfile):
    try:
        with open(keyfile, 'r') as f:
            api_key = f.readline().strip()
        return api_key

    except FileNotFoundError:
        print("Key file not found. Please make sure the file exists.")

    except Exception as e:
        print("An error occurred opening the API key file: ", e)

def fetchNews(feed, entryIndex):
    NewsFeed = feedparser.parse(feed)
    entry = NewsFeed.entries[entryIndex]
    return (entry.title + ". " + entry.summary + ". " + entry.content[0].value)

def generateSummary(input, length):
    summary = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[{"role":"user", "content": "In " + str(length) + " words summarize: " + input}]
    )
    return summary.choices[0].message.content + " "

def editPodcast(podcast):
    edit = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[{"role":"user", "content": "Improve this podcast script, add transitions between stories and outro, do not alter facts:\n " + podcast }]
    )
    return edit.choices[0].message.content + " "


# Init TTS
model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
tts = TTS(model_name)

# Init OpenAI
openai.api_key = load_KEY("API_KEY")
# print("The following AI models are available via the API:")
# availableModels = openai.Model.list()
# print(availableModels)


# Get News


podcastIntro = "Welcome to Gee Pee Tee Daily. Your Artificial Inteligence powered flash briefing on today's top stories. Let's dive in."
podcast = podcastIntro
podcast += ("Today is " + getStringDate() + ". ")
podcast += "From the new york times, "

for story in range(1):

    news = fetchNews(nytRSS,story)
    print("\n\nNews: ", news)
    podcast += generateSummary(news,20)

podcast += "Now, news from hackaday: "

for hackaday in range(1):
    news = fetchNews(hackadayRSS, hackaday)
    podcast += generateSummary(news, 30)

podcast += "From Ars Technica: "

for ars in range(1):
    news = fetchNews(arsTechnicaRSS, ars)
    podcast += generateSummary(news, 30)

# print("\n\nAI Summary: ")
# print(podcast, "\n\n")



# tts.tts_to_file(text=podcast, file_path="output.wav")

# Load the WAV file
# sound = AudioSegment.from_file("output.wav")

# Play the sound
# play(sound)

print("______ EDITED PODCAST _________")
editedPodcast = editPodcast(podcast)
print(editedPodcast)
# tts.tts_to_file(text=editedPodcast, file_path="output.wav")
# sound = AudioSegment.from_file("output.wav")
# play(sound)

googleTTS(editedPodcast, "podcast.mp3")
sound = AudioSegment.from_file("podcast.mp3")
play(sound)

