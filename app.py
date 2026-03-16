import tkinter as tk
from tkinter import messagebox
import webbrowser

class Button:
    # Improved button class for CronTab GUI
    def __init__(self, text, background_color="#FF0000", foreground_color="#FFFFFF", url=None):
        self.text = text
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.url = url

    def create_button(self, root, command=None):
        if self.url:
            command = lambda: webbrowser.open(self.url)
        btn = tk.Button(
            root, 
            text=self.text, 
            bg=self.background_color, 
            fg=self.foreground_color, 
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=20,
            pady=5,
            command=command
        )
        return btn

class CronTabGUI:
    def __init__(self, title="AI Search Hub", size="500x300"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.configure(bg="#f0f0f0")
        self.setup_gui()

    def setup_gui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="AI Search Hub", 
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=10)

        # Search bar frame
        search_frame = tk.Frame(self.root, bg="#f0f0f0")
        search_frame.pack(pady=10)

        # Search entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 12),
            width=40,
            relief="solid",
            bd=1
        )
        self.search_entry.pack(pady=5)
        self.search_entry.bind('<Return>', self.on_search)

        # Search button
        search_btn = tk.Button(
            search_frame,
            text="Search",
            bg="#4285f4",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            command=self.on_search
        )
        search_btn.pack()

        # AI Links/Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(pady=20)

        # Define 5 AI links
        ai_buttons = [
            Button("Claude.ai", "#ff6b6b", "#fff", "https://claude.ai"),
            Button("ChatGPT", "#4ecdc4", "#fff", "https://chatgpt.com"),
            Button("Perplexity", "#45b7d1", "#fff", "https://www.perplexity.ai"),
            Button("Gemini", "#96ceb4", "#333", "https://gemini.google.com"),
            Button("Grok", "#ffeaa7", "#333", "https://grok.x.ai")
        ]

        # Create and pack buttons
        for btn_config in ai_buttons:
            btn = btn_config.create_button(self.root)
            btn.pack(pady=5, padx=10, fill="x")

    def on_search(self, event=None):
        query = self.search_var.get().strip()
        if query:
            # Open search in default browser (you can customize this)
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            messagebox.showinfo("Search", f"Searching for: {query}")
        else:
            messagebox.showwarning("No Query", "Please enter a search term!")

    def run(self):
        self.root.mainloop()

# Run the GUI
if __name__ == "__main__":
    app = CronTabGUI("AI Search Hub", "500x400")
    app.run()
