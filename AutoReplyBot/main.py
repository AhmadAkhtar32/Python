import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import random

# --- ADVANCED AI-LIKE BOT RESPONSES ---
def get_reply(msg):
    msg = msg.lower()

    basic_responses = {
        "hello": "Hello! 👋 How can I assist you today?",
        "hi": "Hi there! 😊 What can I do for you?",
        "how are you": "I'm functioning perfectly! Thanks for asking 🤖",
        "your name": "I'm SmartBot — your intelligent assistant!",
        "who are you": "I'm SmartBot, built using Python and Tkinter!",
        "bye": "Goodbye! 👋 Take care!",
        "thanks": "You're welcome! 😊",
        "thank you": "Happy to help! 🤖",
        "help": "Sure! Tell me what you need assistance with.",
    }

    # keyword-based answers
    for key in basic_responses:
        if key in msg:
            return basic_responses[key]

    # fallback smart replies
    fallback = [
        "Interesting! Tell me more 🤔",
        "I'm not fully sure, but I can try to help!",
        "Can you explain it another way?",
        "Hmm… I don't understand that yet 😅",
        "Let me think... 🤖",
    ]

    return random.choice(fallback)


# --- TYPING ANIMATION ---
def type_message(widget, message, tag):
    widget.config(state=tk.NORMAL)
    widget.insert(tk.END, message[0], tag)
    widget.config(state=tk.DISABLED)
    widget.update()

    for i in range(1, len(message)):
        widget.config(state=tk.NORMAL)
        widget.insert(tk.END, message[i], tag)
        widget.config(state=tk.DISABLED)
        widget.update()
        widget.after(10)  # typing speed


# --- SEND MESSAGE FUNCTION ---
def send_message(event=None):
    user_msg = entry_field.get().strip()
    if user_msg == "":
        return

    timestamp = datetime.now().strftime("[%H:%M] ")

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, timestamp + "You: " + user_msg + "\n", "user")
    chat_box.config(state=tk.DISABLED)

    entry_field.delete(0, tk.END)

    bot_reply = get_reply(user_msg)

    chat_box.config(state=tk.NORMAL)
    type_message(chat_box, timestamp + "Bot: " + bot_reply + "\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)


# --- CLEAR CHAT ---
def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete(1.0, tk.END)
    chat_box.config(state=tk.DISABLED)


# --- SAVE CHAT TO FILE ---
def save_chat():
    content = chat_box.get(1.0, tk.END).strip()
    if content == "":
        messagebox.showwarning("Warning", "Chat is empty!")
        return

    with open("chat_history.txt", "w", encoding="utf-8") as f:
        f.write(content)
    messagebox.showinfo("Saved", "Chat saved as chat_history.txt")


# --- DARK MODE ---
dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.config(bg="#1e1e1e")
        entry_frame.config(bg="#1e1e1e")
        chat_box.config(bg="#2d2d2d", fg="white")
        entry_field.config(bg="#3a3a3a", fg="white")
        send_button.config(bg="#4CAF50")
        clear_button.config(bg="#444")
        save_button.config(bg="#444")
        theme_button.config(text="Light Mode ☀️")
    else:
        root.config(bg="#f0f0f0")
        entry_frame.config(bg="#f0f0f0")
        chat_box.config(bg="white", fg="black")
        entry_field.config(bg="white", fg="black")
        send_button.config(bg="#4CAF50")
        clear_button.config(bg="#ddd")
        save_button.config(bg="#ddd")
        theme_button.config(text="Dark Mode 🌙")


# --- GUI WINDOW ---
root = tk.Tk()
root.title("SmartBot 🤖 (Advanced Chatbot)")
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# --- CHAT AREA ---
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED,
                                     bg="white", fg="black", font=("Arial", 11))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")

# --- ENTRY AREA ---
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(fill=tk.X, padx=10, pady=5)

entry_field = tk.Entry(entry_frame, font=("Arial", 12))
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry_field.bind("<Return>", send_message)

send_button = tk.Button(entry_frame, text="Send", command=send_message,
                        bg="#4CAF50", fg="white", font=("Arial", 11), width=7)
send_button.pack(side=tk.RIGHT, padx=(5, 0))

# --- BOTTOM BUTTONS ---
bottom_frame = tk.Frame(root, bg="#f0f0f0")
bottom_frame.pack(fill=tk.X, pady=8)

clear_button = tk.Button(bottom_frame, text="Clear Chat", command=clear_chat,
                         width=12, bg="#ddd")
clear_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(bottom_frame, text="Save Chat", command=save_chat,
                        width=12, bg="#ddd")
save_button.pack(side=tk.LEFT, padx=10)

theme_button = tk.Button(bottom_frame, text="Dark Mode 🌙", command=toggle_theme,
                         width=12, bg="#ddd")
theme_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
