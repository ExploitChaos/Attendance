import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

# 1. Define the main application class (OOP approach)
class BasicTkinterApp:
    def __init__(self, master):
        # Configure the main window
        self.master = master
        master.title("Basic Tkinter Demo")
        master.geometry("1920x1080") # Set initial window size

        # --- 2. Advanced Feature: Use a Tabbed Interface (ttk.Notebook) ---
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        # Create two tabs
        self.main_tab = ttk.Frame(self.notebook)
        self.log_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.main_tab, text="Input & Output")
        self.notebook.add(self.log_tab, text="Activity Log")

        # Call methods to build the content for each tab
        self.build_main_tab()
        self.build_log_tab()
        
        # Initialize an activity counter for the cool feature
        self.activity_count = 0

    # Method to build content for the main tab
    def build_main_tab(self):
        # 3. TEXT BOX (Input)
        input_label = tk.Label(self.main_tab, text="Enter a simple word (e.g., 'hello'):")
        input_label.pack(pady=5, padx=10, anchor="w")
        
        # The actual text entry widget
        self.input_text = tk.Entry(self.main_tab, width=40)
        self.input_text.pack(pady=5, padx=10, fill="x")

        # 4. BUTTON (Action)
        self.process_button = tk.Button(
            self.main_tab, 
            text="Process Input & Log", 
            command=self.process_and_log_input, 
            bg="#4CAF50", # Cool button color
            fg="white"    # White text
        )
        self.process_button.pack(pady=10, padx=10)
        
        # 5. OUTPUT DISPLAY (Dynamic Label)
        output_label = tk.Label(self.main_tab, text="Last Output Status:")
        output_label.pack(pady=5, padx=10, anchor="w")
        
        # A dynamic label to show the last result
        self.output_status = tk.StringVar(self.master, value="Awaiting input...")
        self.output_display = tk.Label(
            self.main_tab, 
            textvariable=self.output_status, 
            fg="blue", 
            font=('Arial', 10, 'bold')
        )
        self.output_display.pack(pady=5, padx=10, fill="x")
        
    # Method to build the cool log feature tab
    def build_log_tab(self):
        # COOL FEATURE: Scrolled Text Box (Output History/Log)
        log_label = tk.Label(self.log_tab, text="Application Activity Log:")
        log_label.pack(pady=5, padx=10, anchor="w")
        
        # A ScrolledText widget is a Tkinter Text widget with a scrollbar
        self.log_area = scrolledtext.ScrolledText(
            self.log_tab, 
            width=50, 
            height=15, 
            wrap=tk.WORD # Ensures lines wrap nicely
        )
        self.log_area.pack(pady=5, padx=10, fill="both", expand=True)
        self.log_area.insert(tk.END, "Application started successfully.\n")
        self.log_area.config(state=tk.DISABLED) # Make it read-only
        
    # The function that runs when the button is clicked
    def process_and_log_input(self):
        user_input = self.input_text.get()
        self.activity_count += 1
        
        # --- Advanced Feature: Input Validation ---
        if not user_input.strip():
            messagebox.showerror("Error", "Input cannot be empty!")
            self.output_status.set("Error: Empty input.")
            self.update_log(f"[{self.activity_count}] ERROR: Empty input provided.")
            return

        # Simple processing logic
        processed_data = user_input.upper() + "!"
        
        # Update the dynamic label (Output)
        self.output_status.set(f"Processed: {processed_data}")
        
        # Update the log (Cool Feature)
        self.update_log(f"[{self.activity_count}] Input: '{user_input}'. Output: {processed_data}")

    # Helper method to write to the ScrolledText log area
    def update_log(self, message):
        self.log_area.config(state=tk.NORMAL) # Temporarily make it writable
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END) # Scroll to the bottom
        self.log_area.config(state=tk.DISABLED) # Make it read-only again

# --- Run the application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicTkinterApp(root)
    root.mainloop()