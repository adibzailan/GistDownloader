import requests
import os
from pathlib import Path

def download_gists(username, token, output_file):
    # Get all gists for the user
    url = f"https://api.github.com/users/{username}/gists"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    gists = response.json()

    # Create a single file to store all gist contents
    with open(output_file, "w", encoding="utf-8") as outfile:
        for gist in gists:
            outfile.write(f"Gist ID: {gist['id']}\n")
            outfile.write(f"Description: {gist['description']}\n\n")

            for filename, file_info in gist['files'].items():
                outfile.write(f"File: {filename}\n")
                file_content = requests.get(file_info['raw_url']).text
                outfile.write(file_content)
                outfile.write("\n\n" + "="*50 + "\n\n")

    print(f"All gists have been downloaded and combined into '{output_file}'")

if __name__ == "__main__":
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub personal access token: ")

    # Ask for the file name
    file_name = input("Enter the name for the output file (e.g., my_gists.txt): ")
    if not file_name:
        file_name = "all_gists.txt"  # Default file name if none provided

    # Ask for output file location
    output_location = input("Enter the output file location (press Enter for desktop): ")
    if not output_location:
        # Use desktop as default location
        desktop = Path.home() / "Desktop"
        output_location = desktop
    else:
        output_location = Path(output_location)

    # Combine the location and file name
    full_output_path = output_location / file_name

    # Ensure the directory exists
    full_output_path.parent.mkdir(parents=True, exist_ok=True)

    download_gists(username, token, str(full_output_path))
