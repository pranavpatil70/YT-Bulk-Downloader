# Video Downloader Script

This Python script allows you to download videos from a list of URLs using the `yt-dlp` library. It is designed to be simple, efficient, and easy to use. Below, you'll find all the information you need to get started with this script.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Customization](#customization)
6. [Error Handling](#error-handling)
7. [License](#license)

---

## Features
- **Batch Downloading**: Download multiple videos by providing a list of URLs.
- **Best Quality**: Automatically selects the best available MP4 format for each video.
- **Custom Naming**: Saves videos with their original titles as filenames.
- **Error Handling**: Gracefully handles errors during the download process.

---

## Prerequisites
Before running the script, ensure you have the following installed:
- **Python 3.6 or higher**
- **yt-dlp**: A powerful YouTube downloader library.

---

## Installation
1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Install `yt-dlp`**:
   Run the following command to install the required library:
   ```bash
   pip install yt-dlp
   ```

3. **Clone or Download the Script**:
   - Clone this repository or download the script to your local machine.

---

## Usage
1. **Add Video URLs**:
   Open the script and add the URLs of the videos you want to download to the `video_urls` list:
   ```python
   video_urls = [
       "https://www.youtube.com/watch?v=example1",
       "https://www.youtube.com/watch?v=example2",
       # Add more URLs here
   ]
   ```

2. **Run the Script**:
   Execute the script using Python:
   ```bash
   python download_videos.py
   ```

3. **Check the Downloads**:
   The videos will be saved in the same directory as the script, with their titles as filenames.

---

## Customization
You can customize the script to suit your needs:
- **Change Output Format**:
  Modify the `format` option in the `ydl_opts` dictionary to download videos in a different format or quality.
  ```python
  ydl_opts = {
      'format': 'best[ext=mp4]',  # Change to 'bestvideo+bestaudio' for best quality
      'outtmpl': '%(title)s.%(ext)s',
  }
  ```

- **Change Output Directory**:
  Add the `outtmpl` option with a directory path to save videos in a specific folder:
  ```python
  ydl_opts = {
      'format': 'best[ext=mp4]',
      'outtmpl': 'downloads/%(title)s.%(ext)s',  # Saves videos in a 'downloads' folder
  }
  ```

---

## Error Handling
The script includes basic error handling to ensure it continues downloading even if one URL fails. If an error occurs, it will print the error message and move on to the next URL.

---

## License
This project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

---

## Support
If you encounter any issues or have questions, feel free to open an issue on GitHub or reach out to the maintainers.

---

Enjoy downloading your videos! 🎥