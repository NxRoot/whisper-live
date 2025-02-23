# Whisper Live (Offline Speech Recognition)

This project uses [speech_recognition](https://pypi.org/project/SpeechRecognition/) and [faster_whisper](https://github.com/SYSTRAN/faster-whisper) to record live speech and transcribe it into text.

<img src="https://i.ibb.co/Y4ZJB8Y8/whisper-live.png" style="width: 80%;"></img>

## How to Install
| Exe    | Description | Releases |
| -------- | ------- | ------- |
| <a href="https://github.com/NxRoot/soundboard-x-pro/releases/download/release/Soundboard.X.Pro-win32-x64.zip"><img style="min-width: 40px;min-height: 40px; width: 40px;" src="https://i.ibb.co/CsXKQZtX/img.png"/></a> | Download the latest version   | [Download](https://github.com/NxRoot/soundboard-x-pro/releases/download/release/Soundboard.X.Pro-win32-x64.zip)    |


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

#### Build into Executable

```
pyinstaller --name wl --onefile main.py --icon icon.ico --add-data "model;model"
```

## Custom Execution

#### Debug Logs
```
.\wl.exe --verbose > log.txt
```

