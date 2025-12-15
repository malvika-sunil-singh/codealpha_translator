import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import pyttsx3

# Function to translate text
def translate_text():
    text = text_input.get("1.0", tk.END).strip()
    src_lang = src_var.get()
    dest_lang = dest_var.get()
    
    if not text:
        result_label.config(text="Please enter text to translate.", fg="red")
        return
    
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    
    result_label.config(text=translated.text, fg="black")
    
    # Text-to-speech
    engine = pyttsx3.init()
    engine.say(translated.text)
    engine.runAndWait()

# Function to copy translated text
def copy_text():
    translated_text = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(translated_text)
    root.update()
    result_label.config(text="Copied to clipboard!", fg="green")

# Main GUI window
root = tk.Tk()
root.title("🌍 Language Translation Tool")
root.geometry("600x500")
root.config(bg="#f0f8ff")  # light blue background

# Fonts and styles
font_title = ("Helvetica", 18, "bold")
font_label = ("Arial", 12)
font_button = ("Arial", 12, "bold")

# Title
tk.Label(root, text="Language Translation Tool", font=font_title, bg="#f0f8ff").pack(pady=10)

# Text input
tk.Label(root, text="Enter Text:", font=font_label, bg="#f0f8ff").pack()
text_input = tk.Text(root, height=6, width=60, font=("Arial", 12))
text_input.pack(pady=5)

# Language selection
frame_lang = tk.Frame(root, bg="#f0f8ff")
frame_lang.pack(pady=10)

src_var = tk.StringVar(value="en")
dest_var = tk.StringVar(value="es")

tk.Label(frame_lang, text="Source Language:", font=font_label, bg="#f0f8ff").grid(row=0, column=0, padx=5)
src_menu = ttk.Combobox(frame_lang, textvariable=src_var, values=list(LANGUAGES.keys()), width=10)
src_menu.grid(row=0, column=1, padx=5)

tk.Label(frame_lang, text="Target Language:", font=font_label, bg="#f0f8ff").grid(row=0, column=2, padx=5)
dest_menu = ttk.Combobox(frame_lang, textvariable=dest_var, values=list(LANGUAGES.keys()), width=10)
dest_menu.grid(row=0, column=3, padx=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f8ff")
frame_buttons.pack(pady=10)

translate_btn = tk.Button(frame_buttons, text="Translate 🌐", font=font_button, bg="#4caf50", fg="white", command=translate_text, width=15)
translate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(frame_buttons, text="Copy 📋", font=font_button, bg="#2196f3", fg="white", command=copy_text, width=15)
copy_btn.grid(row=0, column=1, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", wraplength=550, justify="center")
result_label.pack(pady=20)

root.mainloop()