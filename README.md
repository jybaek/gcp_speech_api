# gcp_Speech_api

## 테스트 음성 파일 생성
wav 파일을 raw 형태로 변환
```bash
$ sox hello.wav --channels=1 --rate 16k --bits 16 test.raw
```

## Usage
```bash
$ python3 speech.py
```
