[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Google Cloud Platform (GCP) - speech api
관련 글과 자세한 설명은 [여기 블로그](http://jybaek.tistory.com/671)를 참고하도록 한다. 

## GCP Prerequisite
### Authentication
```bash
$ gcloud auth application-default login
```

### Install Dependencies
```bash
$ pip install -r requirements.txt
```

# Usage

## 음성파일 인식
파일을 텍스트로 통째로 변환하는 방식은 아래와 같이 진행한다.
```bash
$ python speech.py
Transcript: 안녕 하세요 좋은 아침입니다
```

다음은 파일을 `streaming` 방식으로 변환하는 방식이다.
```bash
$ python speech_streaming.py
====================
transcript: 안녕 하세요 좋은 아침입니다
confidence: 0.5344622135162354
```

## 실시간 음성 인식
`pyaudio` 를 설치해야 하는데 `portAudio` 와 *dependency* 가 존재하기 때문에 아래 링크를 참고해서
먼저 설치하도록 한다.

https://stackoverflow.com/a/33821084/4599185

설치가 끝났으면 아래와 같이 실행하면 되는데 음성인식을 대기중인 상태이므로 마이크를 통해
음성을 전달하면 된다.
```bash
$ python transcribe_streaming_mic.py
```

이 코드는 `googlecloudplatform` 에 등록되어있는 예제 코드를 *language* 만 변경해서 사용한 것이므로 참고하도록 한다.
