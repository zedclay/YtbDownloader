import os
from pytube import YouTube

# Function to extract width from resolution (e.g., '1280x720' -> 1280)
def extract_width(resolution):
    try:
        return int(resolution.split('x')[0])
    except ValueError:
        return 0

# Function to display available resolutions for a YouTube video
def display_available_resolutions(video_url):
    yt = YouTube(video_url)
    available_streams = yt.streams.filter(file_extension='mp4')
    resolutions = [stream.resolution for stream in available_streams if stream.resolution]
    unique_resolutions = sorted(set(resolutions), key=extract_width, reverse=True)
    print("Available resolutions:")
    for i, resolution in enumerate(unique_resolutions, start=1):
        print(f"{i}. {resolution}")
    return unique_resolutions

# Function to download YouTube video with a specific resolution
def download_video(video_url, resolution, output_path):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(res=f"{resolution}").first()
    video_stream.download(output_path=output_path)
    print("Download completed successfully.")

# Function to download YouTube video as MP3
def download_audio(video_url, output_path):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)
    print("Download completed successfully.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    resolutions = display_available_resolutions(video_url)

    download_option = int(input("Enter 1 to download as MP3, 2 to download as MP4: "))

    if download_option == 1:
        output_path = "path_to_save_downloaded_mp3_files"
        download_audio(video_url, output_path)
    elif download_option == 2:
        resolution_choice = int(input("Enter the number corresponding to your desired resolution: "))
        selected_resolution = resolutions[resolution_choice - 1]
        output_path = "path_to_save_downloaded_mp4_files"
        download_video(video_url, selected_resolution, output_path)
    else:
        print("Invalid download option. Please enter 1 for MP3 or 2 for MP4.")
