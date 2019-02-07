#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os
import sys
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

from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    args.audio_path)

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code=args.language_code)

# Detects speech in the audio file
response = client.recognize(config, audio)
alternatives = response.results[0].alternatives

for alternative in alternatives:
    print('{} : {}'.format(args.audio_path, alternative.transcript))
