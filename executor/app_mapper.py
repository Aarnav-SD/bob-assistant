APP_MAP = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "spotify": "spotify",
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "vscode": "code",
    "cmd": "cmd"
}

def resolve_app(app_name):
    return APP_MAP.get(app_name.lower(), app_name)