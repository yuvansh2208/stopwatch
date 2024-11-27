import tkinter as tk

# Functionality for the time counter
class TimeCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Counter")
        self.root.geometry("300x200")

        self.running = False
        self.time_elapsed = 0

        # Label to display the time
        self.label = tk.Label(self.root, text="00:00:00", font=("Arial", 40), bg="black", fg="white")
        self.label.pack(pady=20)

        # Start, Stop, Reset buttons
        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 15), command=self.start)
        self.start_button.pack(side="left", padx=20)

        self.stop_button = tk.Button(self.root, text="Stop", font=("Arial", 15), command=self.stop)
        self.stop_button.pack(side="left", padx=20)

        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 15), command=self.reset)
        self.reset_button.pack(side="left", padx=20)

    def update_time(self):
        if self.running:
            # Increment time by 1 second
            self.time_elapsed += 1

            # Convert time_elapsed to hours, minutes, and seconds
            hours = self.time_elapsed // 3600
            minutes = (self.time_elapsed % 3600) // 60
            seconds = self.time_elapsed % 60

            # Update the label to display the formatted time
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

            # Schedule the update_time method to run again after 1000 milliseconds (1 second)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

# Create the root window and run the application
root = tk.Tk()
time_counter = TimeCounter(root)
root.mainloop()
