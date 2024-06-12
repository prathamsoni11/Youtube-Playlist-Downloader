# YouTube Playlist Downloader

This Python script downloads videos from a YouTube playlist in 1080p or the highest available resolution below 1080p, and zips them into a single file. It uses the `pytube` library to download videos and the `python-dotenv` library to load environment variables from a `.env` file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prathamsoni11/Youtube-Playlist-Downloader.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Youtube-Playlist-Downloader
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install pytube python-dotenv
   ```

5. Create a `.env` file in the project directory and add your playlist URL and desired zip file name:
   ```plaintext
   PLAYLIST_URL=YOUR_PLAYLIST_URL_HERE
   ZIP_FILE_NAME=YOUR_ZIP_FILE_NAME_HERE
   ```

6. Run the script:
   ```bash
   python3 script.py
   ```

7. Once the script finishes, deactivate the virtual environment:
   ```bash
   deactivate
   ```

## Configuration

You can customize the script by editing the `.env` file with your playlist URL and desired zip file name. Ensure that the `PLAYLIST_URL` is the URL of the YouTube playlist you want to download, and `ZIP_FILE_NAME` is the desired name of the zip file.

## Dependencies

- [pytube](https://python-pytube.readthedocs.io/en/latest/) - For downloading YouTube videos.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For loading environment variables from a `.env` file.
