# Whisper Live (Offline Speech Recognition)

This project uses [speech_recognition](https://pypi.org/project/SpeechRecognition/) and [faster_whisper](https://github.com/SYSTRAN/faster-whisper) to record live speech and transcribe it into text.

<img src="https://i.ibb.co/Y4ZJB8Y8/whisper-live.png" style="width: 80%;"></img>

## How to Install
| Exe    | Description | Releases |
| -------- | ------- | ------- |
| <a href="https://github.com/NxRoot/whisper-live/releases/tag/latest"><img style="min-width: 40px;min-height: 40px; width: 40px;" src="https://i.ibb.co/CsXKQZtX/img.png"/></a> | Download the latest version   | [Download](https://github.com/NxRoot/whisper-live/releases/tag/latest)    |


## Build from Source

#### Create a Virtual Environment

```
python -m venv venv
```

#### Activate the Virtual Environment

```
.\venv\Scripts\activate
```

#### Install required libraries

```
pip install -r requirements.txt
```

#### Test the application

```
python main.py
```

#### Build into Executable

```
pyinstaller --name wl --onefile main.py --icon icon.ico --add-data "model;model"
```

## Custom Execution

> This executable can be called from a terminal or any other app.

#### Default
```
.\wl.exe
```

#### Debug Logs
```
.\wl.exe --verbose > log.txt
```

