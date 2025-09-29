import tkinter as tk
from tkinter import ttk

class HelloTranslatorApp:
    """
    A simple Tkinter application to translate "Hello" into several languages.
    Uses a class structure and updates a single label upon button clicks.
    """
    def __init__(self, master):
        # 1. Setup the main window
        self.master = master
        master.title("The Hello Translator")
        master.geometry("400x350")
        master.resizable(False, False)
        master.configure(bg='#f0f4f8') # Light background

        # Use a modern-looking style for better aesthetics
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Inter', 12, 'bold'), padding=10, background='#4a90e2', foreground='white', borderwidth=0, relief='flat')
        style.map('TButton',
                  background=[('active', '#3a78c2')],
                  relief=[('pressed', 'sunken'), ('active', 'flat')])
        style.configure('TLabel', font=('Inter', 16), background='#f0f4f8', foreground='#333333')
        style.configure('Header.TLabel', font=('Inter', 20, 'bold'), foreground='#1e3a8a')
        style.configure('Footer.TLabel', font=('Inter', 18, 'italic'), background='#ffffff', foreground='#1e3a8a', padding=15)

        # Dictionary of translations
        self.greetings = {
            "English": "Hello",
            "Spanish": "¡Hola!",
            "French": "Bonjour",
            "German": "Guten Tag",
            "Italian": "Ciao",
            "Japanese": "Konnichiwa (こんにちは)",
            "Mandarin": "Nǐ hǎo (你好)",
            "Russian": "Privet (Привет)"
        }

        # 2. Main Title/Header Label
        header_label = ttk.Label(master, text="Select a Language", style='Header.TLabel')
        header_label.pack(pady=(20, 10))

        # 3. Button Frame (for organizing the buttons neatly)
        self.button_frame = ttk.Frame(master, padding="15 15 15 15", relief="groove", borderwidth=1, style='TFrame')
        self.button_frame.pack(pady=10)

        # 4. Create and place buttons in a grid layout within the frame
        col = 0
        row = 0
        for language, greeting in self.greetings.items():
            # Use a lambda function to pass the language name to the command
            button = ttk.Button(
                self.button_frame,
                text=language,
                command=lambda lang=language: self.update_translation(lang)
            )
            # Arrange buttons in two columns
            button.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

            col += 1
            if col > 1:
                col = 0
                row += 1

        # 5. Single Label at the bottom (This is where the translation will appear)
        self.translation_label = ttk.Label(master, text="Click a button to translate 'Hello'!", style='Footer.TLabel', anchor='center')
        self.translation_label.pack(fill='x', padx=15, pady=(20, 20))


    def update_translation(self, language):
        """
        Updates the text of the single translation label based on the button clicked.
        """
        greeting = self.greetings.get(language, "Translation not found.")
        new_text = f"The translation is: {greeting}"
        self.translation_label.config(text=new_text)


if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    
    # Initialize the application class
    app = HelloTranslatorApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()