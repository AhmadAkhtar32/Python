import tkinter as tk
from tkinter import scrolledtext

# --- Function for generating auto replies ---
def get_reply(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! 👋 How can I help you today?"
    elif "how are you" in msg:
        return "I'm just a bot, but I'm doing great! 😊"
    elif "your name" in msg:
        return "I'm AutoBot, your friendly assistant!"
    elif "bye" in msg:
        return "Goodbye! 👋 Have a nice day!"
    elif "thank" in msg:
        return "You're welcome! 🤖"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# --- Function for sending messages ---
def send_message():
    user_msg = entry_field.get()
    if user_msg.strip() == "":
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_msg + "\n", "user")
    entry_field.delete(0, tk.END)

    bot_reply = get_reply(user_msg)
    chat_box.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# --- GUI setup ---
root = tk.Tk()
root.title("Auto Reply Bot 🤖")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# --- Chat area ---
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="#000000", font=("Arial", 11))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")

# --- Entry area ---
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(fill=tk.X, padx=10, pady=5)

entry_field = tk.Entry(entry_frame, font=("Arial", 12))
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
entry_field.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 11), width=8)
send_button.pack(side=tk.RIGHT)

# --- Run the app ---
root.mainloop()
