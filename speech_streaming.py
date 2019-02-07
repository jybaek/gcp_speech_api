#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os
import argparse
from opts import add_basic_args

parser = argparse.ArgumentParser(description='speech to text')
parser = add_basic_args(parser)
args = parser.parse_args()

if args.language_code not in ('ko-KR', 'en-US'):
    raise ValueError('Unknown language-code')

if not os.path.isfile(args.audio_path):
    raise ValueError('No such file: ', args.audio_path)

# Imports the Google Cloud client library
try:
    from google.cloud import speech
except ImportError:
    raise ImportError('Error import speech error')

from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()
config = types.RecognitionConfig(
    encoding='LINEAR16',
    language_code=args.language_code,
    sample_rate_hertz=16000)

# Loads the audio into memory
with io.open(args.audio_path, 'rb') as stream:
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
