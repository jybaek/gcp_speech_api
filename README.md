# Google Cloud Platform (GCP) - speech api
http://jybaek.tistory.com/671

## 테스트 음성 파일 생성
wav 파일을 raw 형태로 변환
```bash
$ sox hello.wav --channels=1 --rate 16k --bits 16 test.raw
```

## Usage
```bash
$ python3 speech.py
Transcript: 안녕 하세요 좋은 아침입니다
$ python3 speech_streaming.py
====================
transcript: 안녕 하세요 좋은 아침입니다
confidence: 0.5344622135162354
```
