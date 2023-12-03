import tkinter as tk
import random
import time

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title("Typing Speed Test")

        self.words = ['programming', 'coding', 'algorithm', 'systems', 'python', 'software']
        self.current_word = None
        self.start_time = None

        self.label = tk.Label(root, text="Welcome to Typing Speed Test!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_result)

        self.start_button = tk.Button(root, text="Start", command=self.start_game, font=("Helvetica", 12))
        self.start_button.pack(pady=10)

    def start_game(self):
        self.current_word = random.choice(self.words)
        self.label.config(text=self.current_word, fg="black")
        self.start_time = time.time()
        self.entry.delete(0, 'end')
        self.entry.focus_set()
        self.start_button.config(state=tk.DISABLED)

    def check_result(self, event):
        user_input = self.entry.get()
        end_time = time.time()
        time_taken = end_time - self.start_time

        if user_input == self.current_word:
            self.label.config(text=f"Time taken: {time_taken:.2f} seconds", fg="green")
        else:
            self.label.config(text="Wrong Input", fg="red")

        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
