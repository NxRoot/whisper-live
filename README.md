# Whisper Live (Offline Speech Recognition)

This project uses [speech_recognition](https://pypi.org/project/SpeechRecognition/) and [faster_whisper](https://github.com/SYSTRAN/faster-whisper) to record live speech and transcribe it into text.

<img src="https://i.ibb.co/Y4ZJB8Y8/whisper-live.png" style="width: 80%;"></img>

## How to Install
| Exe    | Description | Releases |
| -------- | ------- | ------- |
| <a href="https://github.com/NxRoot/whisper-live/releases/tag/latest"><img style="min-width: 40px;min-height: 40px; width: 40px;" src="https://i.ibb.co/CsXKQZtX/img.png"/></a> | Download the latest version   | [Download](https://github.com/NxRoot/whisper-live/releases/tag/latest)    |


## Build from Source

```
git clone https://github.com/NxRoot/whisper-live.git
```

<details>
<summary>Create a Virtual Environment</summary>
  
###### Win32
```
python -m venv venv
```
###### MacOS
```
python3 -m venv venv
```

</details>

<details>
<summary>Activate the Virtual Environment</summary>
  
###### Win32
```
.\venv\Scripts\activate
```
###### MacOS
```sh
source venv/lib/activate
```

</details>

<details>
<summary>Install required libraries</summary>

###### Win32
```
pip install -r requirements.txt
```
###### MacOS
```
pip3 install -r requirements.txt
```

</details>

<details>
<summary>Test the application</summary>

###### Win32
```
python main.py
```
###### MacOS
```
python3 main.py
```

</details>

<details>
<summary>Build into Executable</summary>

###### Win32
```
pyinstaller --name wl --onedir main.py --icon icon.ico --add-data "model;model"
```
###### MacOS
```
pyinstaller --name wl --onedir main.py --icon icon.ico --add-data "model:model" --paths=./venv/lib/python3.10/site-packages
```

> Make sure the **--paths** argument is aligned with your python version.

&nbsp;

</details>



## Custom Execution

> This can be executed from a terminal or called from another app.

#### Default
```
wl.exe
```

#### Show Info
```
wl.exe --verbose
```

#### Debug Logs
```
wl.exe --verbose > logs.txt
```

## Call Examples

#### NodeJS
```js
const { join } = require("path");
const { spawn } = require("child_process");

const ps = spawn(join(__dirname, "wl.exe"));

ps.stdout.on("data", (data) => {
  console.log(data);
});

ps.stderr.on("data", (data) => {
  console.error(data);
});

ps.on("close", (code) => {
  console.log(`Process exited with code ${code}`);
});
```

## Important Notes

* Always clone the repo if you wish to build from source.
* The model can take some time to load using portable versions.
* On MacOS the SpeechRecognition module requires [PortAudio](https://formulae.brew.sh/formula/portaudio) installed.

## &nbsp;
⭐ If you find this useful!
