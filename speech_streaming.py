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
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()
config = types.RecognitionConfig(
    encoding='LINEAR16',
    language_code='ko-KR',
    sample_rate_hertz=16000)

# Loads the audio into memory
with io.open("./test.raw", 'rb') as stream:
    requests = [types.StreamingRecognizeRequest(
        audio_content=stream.read(),
    )]

config=types.StreamingRecognitionConfig(config=config)
responses = client.streaming_recognize(config,requests)

for response in responses:
    for result in response.results:
        for alternative in result.alternatives:
            print('=' * 20)
            print('transcript: {}'.format(alternative.transcript))
            print('confidence: {}'.format(alternative.confidence))
