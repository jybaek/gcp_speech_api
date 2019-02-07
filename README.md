[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Google Cloud Platform (GCP) - speech api
This is an example using Google's speech to text api. A little more details can be found on the blog below.

http://jybaek.tistory.com/671

## GCP Prerequisite
Perform authentication and resolve associated dependencies.

### Authentication
```bash
$ gcloud auth application-default login
```

### Install Dependencies
```bash
$ pip install -r requirements.txt
```

# Usage

## Audio file recognition
To convert a file to text in its entirety, proceed as follows.
```bash
$ python speech.py
Transcript: 안녕 하세요 좋은 아침입니다
```

The default is to specify _test.raw_ via the `audio-path` option.
Take a look at the options through `help` as below.
```bash
$ python speech.py --help
usage: speech.py [-h] [--audio-path AUDIO_PATH]
                 [--language-code LANGUAGE_CODE]

speech to text

optional arguments:
  -h, --help            show this help message and exit
  --audio-path AUDIO_PATH
                        Audio file to convert to text.
  --language-code LANGUAGE_CODE
                        Language code. ( ko-KR, en-US, etc.. )
```

Here is an example of converting a file to `streaming`.
The options are the same as for _speech.py_.
```bash
$ python speech_streaming.py
====================
transcript: 안녕 하세요 좋은 아침입니다
confidence: 0.5344622135162354
```

## Real-time speech recognition
You need to install `pypaudio`, please refer to the link below to install it first.

https://stackoverflow.com/a/33821084/4599185

After the installation is completed, you can do the following. Speech recognition is pending, so deliver voice over the microphone.
```bash
$ python transcribe_streaming_mic.py
```

Most of the sample code that is registered with `googlecloudplatform` is used.
