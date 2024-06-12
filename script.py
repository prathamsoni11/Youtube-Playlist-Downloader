import os
import shutil
from pytube import Playlist, YouTube
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def sanitize_filename(filename):
    # Remove characters not allowed in filenames
    return "".join([c for c in filename if c.isalnum() or c in (' ', '.', '-')])

def download_video(url, output_path, index):
    yt = YouTube(url)
    # Try to get the 1080p stream first
    stream = yt.streams.filter(file_extension='mp4', resolution='1080p').first()
    
    # If no 1080p stream is found, get the highest available resolution below 1080p
    if stream is None:
        stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
    
    if stream is None:
        print(f"No suitable stream found for {url}")
        return
    
    # Ensure the filename has the .mp4 extension and sanitize it
    title = f"{index:02d} - {yt.title}"
    title = sanitize_filename(title)
    title = title[:255]  # Limit filename length for compatibility with some systems
    title += ".mp4"

    stream.download(output_path=output_path, filename=title)
    print(f"Downloaded: {title}")

def download_playlist(playlist_url, zip_filename, output_path='downloads'):
    playlist = Playlist(playlist_url)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for index, url in enumerate(playlist.video_urls, start=1):
        download_video(url, output_path, index)

    # Create a zip archive of the downloaded videos
    shutil.make_archive(zip_filename, 'zip', output_path)
    print(f"Created zip file: {zip_filename}.zip")

    # Clean up the downloads folder after zipping
    shutil.rmtree(output_path)
    print(f"Cleaned up folder: {output_path}")

if __name__ == '__main__':
    playlist_url = os.getenv('PLAYLIST_URL')
    zip_filename = os.getenv('ZIP_FILE_NAME')
    
    if playlist_url and zip_filename:
        download_playlist(playlist_url, zip_filename)
    else:
        print("Please set the PLAYLIST_URL and ZIP_FILE_NAME in the .env file.")
