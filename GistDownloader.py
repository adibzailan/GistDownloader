import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests
from pathlib import Path

def get_language(filename):
    extension = Path(filename).suffix.lower()
    language_map = {
        '.cs': 'csharp', '.xml': 'xml', '.config': 'xml', '.json': 'json',
        '.html': 'html', '.css': 'css', '.js': 'javascript', '.ts': 'typescript',
        '.sql': 'sql', '.py': 'python', '.addin': 'xml', '.txt': 'plaintext',
        '.md': 'markdown', '.yml': 'yaml', '.yaml': 'yaml', '.sh': 'bash',
        '.bat': 'batch', '.ps1': 'powershell', '.rb': 'ruby', '.java': 'java',
        '.php': 'php', '.go': 'go', '.swift': 'swift', '.kt': 'kotlin',
        '.rs': 'rust', '.cpp': 'cpp', '.c': 'c', '.h': 'cpp', '.hpp': 'cpp',
        '.vb': 'vb', '.fs': 'fsharp', '.r': 'r', '.m': 'matlab',
        '.scala': 'scala', '.groovy': 'groovy', '.pl': 'perl', '.lua': 'lua',
        '.dart': 'dart', '.ex': 'elixir', '.exs': 'elixir', '.hs': 'haskell',
        '.clj': 'clojure', '.erl': 'erlang', '.tex': 'latex',
    }
    return language_map.get(extension, 'plaintext')

def download_gists(username, token, output_file):
    url = f"https://api.github.com/users/{username}/gists"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    gists = response.json()

    with open(output_file, "w", encoding="utf-8") as outfile:
        for gist in gists:
            outfile.write(f"# Gist ID: {gist['id']}\n")
            outfile.write(f"Description: {gist['description']}\n\n")

            for filename, file_info in gist['files'].items():
                language = get_language(filename)
                outfile.write(f"## File: {filename}\n")
                outfile.write(f"```{language}\n")
                file_content = requests.get(file_info['raw_url']).text
                outfile.write(file_content)
                outfile.write("\n```\n\n")

            outfile.write("---\n\n")

def browse_files():
    filename = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
    output_file_var.set(filename)

def download_gists_gui():
    username = username_var.get().strip()
    token = token_var.get().strip()
    output_file = output_file_var.get().strip()

    if not username or not token or not output_file:
        download_button.config(state=tk.NORMAL, text="Error ?", bg="#FF0000", fg="white")
        messagebox.showerror("Error", "Please fill in all fields")
        root.after(2000, lambda: download_button.config(text="Download Gists", bg="#f0f0f0", fg="black"))
        return

    try:
        download_button.config(state=tk.DISABLED, text="Downloading...", bg="#f0f0f0")
        root.update()
        download_gists(username, token, output_file)
        download_button.config(state=tk.NORMAL, text="Gists downloaded", bg="#FF6F61", fg="white")
        root.after(2000, lambda: download_button.config(text="Download Gists", bg="#f0f0f0", fg="black"))
    except Exception as e:
        download_button.config(state=tk.NORMAL, text="Error ?", bg="#FF0000", fg="white")
        messagebox.showerror("Error", str(e))
        root.after(2000, lambda: download_button.config(text="Download Gists", bg="#f0f0f0", fg="black"))

# Set up the main window
root = tk.Tk()
root.title("GitHub Gist Downloader")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

# Create and configure a main frame
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create StringVar for inputs
username_var = tk.StringVar()
token_var = tk.StringVar()
output_file_var = tk.StringVar()

# Username
ttk.Label(main_frame, text="GitHub Username:").grid(column=0, row=0, sticky=tk.W, pady=(0, 5))
ttk.Entry(main_frame, width=50, textvariable=username_var).grid(column=0, row=1, sticky=(tk.W, tk.E), pady=(0, 10))

# Token
ttk.Label(main_frame, text="GitHub Personal Access Token:").grid(column=0, row=2, sticky=tk.W, pady=(0, 5))
ttk.Entry(main_frame, width=50, textvariable=token_var, show="*").grid(column=0, row=3, sticky=(tk.W, tk.E), pady=(0, 10))

# Output File
ttk.Label(main_frame, text="Output File:").grid(column=0, row=4, sticky=tk.W, pady=(0, 5))
output_file_frame = ttk.Frame(main_frame)
output_file_frame.grid(column=0, row=5, sticky=(tk.W, tk.E), pady=(0, 10))
ttk.Entry(output_file_frame, width=40, textvariable=output_file_var).grid(column=0, row=0, sticky=(tk.W, tk.E))
ttk.Button(output_file_frame, text="Browse", command=browse_files).grid(column=1, row=0, sticky=tk.E, padx=(10, 0))

# Set placeholder for output file
output_file_var.set("Click 'Browse' to select output file location")

# Download Button
download_button = tk.Button(main_frame, text="Download Gists", command=download_gists_gui,
                            bg="#f0f0f0", fg="black", font=("Helvetica", 12),
                            padx=10, pady=5)
download_button.grid(column=0, row=6, sticky=tk.W, pady=(10, 0))

# Footer
footer_text = "Beta v0.1 / Made with love in Singapore, Adib Zailan, 2024"
footer_label = ttk.Label(root, text=footer_text, foreground="#888888", font=("Helvetica", 8))
footer_label.grid(column=0, row=1, sticky=(tk.S, tk.W), padx=10, pady=5)

root.mainloop()