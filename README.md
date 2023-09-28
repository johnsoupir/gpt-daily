# gpt-daily

Welcome to gpt-daily - your AI-powered daily news podcast generator!
## Overview

gpt-daily is a Python script that fetches news from various RSS feeds, summarizes them using OpenAI's GPT-3 model, and then converts the summarized news into an audio podcast using Google's Text-to-Speech (TTS) API. The result is a concise and informative daily news podcast, ready for you to listen to!

Features

- Fetches news from popular sources like the New York Times, Hackaday, and Ars Technica.
- Summarizes news articles using the GPT-3 model.
- Converts summarized news into an audio format using Google's TTS.
- Generates a daily podcast with transitions between stories and an outro.

## Getting Started

Clone the Repository:

    git clone https://github.com/johnsoupir/gpt-daily.git

Install Dependencies: Ensure you have the required libraries installed. You can install them using pip:

    pip install openai feedparser pydub google-cloud-texttospeech

API Keys: Make sure you have the necessary API keys for OpenAI and Google Cloud. Place your OpenAI API key in a file named API_KEY.

Run the Script:
    python main.py
Listen to the Podcast: After running the script, you'll find the generated podcast in the podcast.mp3 file.

### Contributing

Feel free to fork this repository, make changes, and submit pull requests.


License

This project is licensed under the terms of GPL3.
