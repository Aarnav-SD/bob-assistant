import tkinter as tk
from tkinter import scrolledtext
import threading
from core.voice_listener import listen_and_transcribe

class BobGUI:
    def __init__(self, root, on_submit_callback):
        self.root = root
        self.root.title("Bob Assistant")
        self.root.geometry("500x450")

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=60)
        self.output_area.pack(pady=10)

        self.input_field = tk.Entry(root, width=60)
        self.input_field.pack(pady=5)
        self.input_field.bind("<Return>", lambda event: self.submit_command())

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.submit_button = tk.Button(self.button_frame, text="Send", command=self.submit_command)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        self.mic_button = tk.Button(self.button_frame, text="🎤 Speak", command=self.voice_command)
        self.mic_button.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(root, text="Status: Idle")
        self.status_label.pack(pady=5)

        self.on_submit_callback = on_submit_callback

    def submit_command(self):
        command = self.input_field.get()
        if command.strip():
            self.input_field.delete(0, tk.END)
            self.display_message("You", command)
            threading.Thread(target=self.on_submit_callback, args=(command,)).start()

    def voice_command(self):
        self.update_status("Listening...")

        def process_voice():
            text = listen_and_transcribe()
            if text:
                self.display_message("You (voice)", text)
                self.on_submit_callback(text)
            else:
                self.display_message("Bob", "I didn't catch that.")
            self.update_status("Idle")

        threading.Thread(target=process_voice).start()

    def display_message(self, sender, message):
        self.output_area.insert(tk.END, f"{sender}: {message}\n")
        self.output_area.yview(tk.END)

    def update_status(self, status):
        self.status_label.config(text=f"Status: {status}")
