import tkinter as tk
from tkinter import scrolledtext
import threading

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10, font=("Times New Roman", 15))
        self.text_area.pack(padx=10, pady=10)

        self.timer_label = tk.Label(self.root, text="Time left: 5s", font=("Times New Roman", 12))
        self.timer_label.pack(padx=10, pady=5)

        self.text_area.bind("<KeyRelease>", self.reset_timer)

        self.timer = None
        self.disappear_time = 5  # seconds
        self.remaining_time = self.disappear_time

        self.update_timer_display()

    def reset_timer(self, event=None):
        if self.timer is not None:
            self.timer.cancel()

        self.remaining_time = self.disappear_time
        self.update_timer_display()
        self.timer = threading.Timer(1, self.countdown)
        self.timer.start()

    def countdown(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()

            self.timer = threading.Timer(1, self.countdown)
            self.timer.start()
        else:
            self.clear_text()

    def clear_text(self):
        self.text_area.delete('1.0', tk.END)
        self.remaining_time = self.disappear_time
        self.update_timer_display()

    def update_timer_display(self):
        self.timer_label.config(text=f"Time left: {self.remaining_time}s")

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
