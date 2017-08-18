# Google Cloud Platform (GCP) - speech api
관련 글과 자세한 설명은 [여기 블로그](http://jybaek.tistory.com/671)를 참고하도록 한다. 

## prerequisite
### Authentication
```bash
$ gcloud auth application-default login
```

### Install Dependencies
```bash
$ pip install google-cloud-speech
```

## 테스트 음성 파일 생성
공식 API 페이지에는 *wav format* 이 지원된다고 명시되어 있지만 정상적으로 인식되지 않음. 
그래서 wav 파일을 raw 형태로 변환하고 사용해야 함. 아래는 *mac* 에서 wav 를 raw 로 변환하는 예제.
```bash
$ sox hello.wav --channels=1 --rate 16k --bits 16 test.raw
```

## Usage
```bash
$ python3 speech.py
Transcript: 안녕 하세요 좋은 아침입니다
$
$ python3 speech_streaming.py
====================
transcript: 안녕 하세요 좋은 아침입니다
confidence: 0.5344622135162354
```
