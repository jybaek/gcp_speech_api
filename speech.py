#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os

# Imports the Google Cloud client library
try:
    from google.cloud import speech
except ImportError:
    print("Error speech import error")
    exit(255)
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'test.raw')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='ko-KR')

# Detects speech in the audio file
response = client.recognize(config, audio)
alternatives = response.results[0].alternatives

for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))
