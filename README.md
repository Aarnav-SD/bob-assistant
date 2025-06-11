# Bob - OS Assistant

Bob is a local offline voice assistant built with Python. It can:
- Launch applications
- Search the web
- Control Spotify
- Adjust volume
- Accept voice or text input
- Create project directories

## Setup

```bash
pip install -r requirements.txt
```
Then run the app using:
```bash
python main.py
```
Note: Make sure to have Ollama's mistral model installed in system
Create custom bob variation of Ollama's mistral using
```bash
ollama create bob -f ./model/Modelfile
ollama run bob
```
To remove bob run:
```bash
ollama rm bob
```
To edit bob's behaviour change the prompt present in the SYSTEM """<prompt>""" of Modelfile
