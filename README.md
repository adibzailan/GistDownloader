# GitHub Gist Downloader

## Overview

The GitHub Gist Downloader is a user-friendly desktop application that allows you to easily download and save all public gists from a specified GitHub user. This tool provides a simple interface to input a GitHub username, personal access token, and output file location, streamlining the process of archiving and reviewing gists.

## Features

- Simple and intuitive graphical user interface
- Download all public gists from a specified GitHub user
- Secure input for GitHub personal access token
- Custom output file selection
- Error handling with visual feedback
- Studio Merpati branding elements

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script by executing (where "XX" is the version to date):
   ```
   python GistDownloader_vXX.py
   ```
2. The GitHub Gist Downloader window will appear.

### Downloading Gists

1. Enter the GitHub username of the account whose gists you want to download.
2. Input your GitHub Personal Access Token. (See [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for instructions on how to obtain one)
3. Click the "Browse" button to select the location and name for the output file.
4. Click the "Download Gists" button to start the download process.
5. A success message will appear briefly on the button when the process is complete. The button will change color to a shade of coral (#FF6F61), which is a nod to the Studio Merpati branding.

## Error Handling

The tool provides error messages in the following situations:
- Any required field is left empty
- Invalid GitHub username or personal access token
- Network connection issues
- Insufficient permissions to write to the selected output location

When an error occurs, the "Download Gists" button will briefly turn red and display an error message.

## Development

This tool is developed using Python and the tkinter library for the graphical user interface. The main script is `GistDownloader.py`.

### Branding

The tool incorporates elements of Studio Merpati branding:
- The success message button color (#FF6F61) is inspired by Studio Merpati's color palette, adding a personal touch to the user interface.
- The error state uses a red background with a sad face icon for clear visual feedback.

### Future Improvements

- Add a progress bar to show download status
- Implement selective gist downloading (e.g., by date range or specific gist IDs)
- Add support for downloading private gists (requires extended permissions)
- Create an executable version for easy distribution across different operating systems
- Implement a dark mode theme option
- Add the ability to update existing gist archives

## Contributing

Contributions to the GitHub Gist Downloader are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

## License

This project is licensed under the MIT License.

## Acknowledgments

Beta v0.1 / Made with love in Singapore, Adib Zailan, 2024
