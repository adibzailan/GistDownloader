#!/usr/bin/env python
import sys
import requests
from pathlib import Path

def get_language(filename):
    extension = Path(filename).suffix.lower()
    language_map = {
        '.cs': 'csharp',
        '.xml': 'xml',
        '.config': 'xml',
        '.json': 'json',
        '.html': 'html',
        '.css': 'css',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.sql': 'sql',
        '.py': 'python',
        '.addin': 'xml',
        '.txt': 'plaintext',
        '.md': 'markdown',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.sh': 'bash',
        '.bat': 'batch',
        '.ps1': 'powershell',
        '.rb': 'ruby',
        '.java': 'java',
        '.php': 'php',
        '.go': 'go',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.rs': 'rust',
        '.cpp': 'cpp',
        '.c': 'c',
        '.h': 'cpp',
        '.hpp': 'cpp',
        '.vb': 'vb',
        '.fs': 'fsharp',
        '.r': 'r',
        '.m': 'matlab',
        '.scala': 'scala',
        '.groovy': 'groovy',
        '.pl': 'perl',
        '.lua': 'lua',
        '.dart': 'dart',
        '.ex': 'elixir',
        '.exs': 'elixir',
        '.hs': 'haskell',
        '.clj': 'clojure',
        '.erl': 'erlang',
        '.tex': 'latex',
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

    print(f"All gists have been downloaded and combined into '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        token = sys.argv[2]
        file_name = sys.argv[3] if len(sys.argv) > 3 else "all_gists.md"
        output_location = Path(sys.argv[4]) if len(sys.argv) > 4 else Path.home() / "Desktop"
    else:
        username = input("Enter your GitHub username: ")
        token = input("Enter your GitHub personal access token: ")
        file_name = input("Enter the name for the output file (e.g., my_gists.md): ") or "all_gists.md"
        output_location = Path(input("Enter the output file location (press Enter for desktop): ") or Path.home() / "Desktop")

    # Ensure the file extension is .md
    file_name = Path(file_name).with_suffix('.md')

    full_output_path = output_location / file_name
    full_output_path.parent.mkdir(parents=True, exist_ok=True)

    download_gists(username, token, str(full_output_path))
