import os
import yt_dlp

def download_youtube_content():
    print("🎬 YouTube Downloader with yt-dlp 🎬")
    print("Download videos or audio files from YouTube with ease!\n")

    # Get user inputs
    url = input("Enter the YouTube playlist or video URL: ").strip()
    if not url:
        print("🚨 URL cannot be empty. Please provide a valid YouTube URL.")
        return

    save_path = input("Enter the folder to save files (or press Enter for the current directory): ").strip() or "."
    download_type = input("Do you want to download 'video' or 'audio' only? (video/audio, default is video): ").strip().lower() or "video"

    # Ensure save_path exists
    os.makedirs(save_path, exist_ok=True)

    # Configure yt-dlp options
    ydl_opts = {
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),  # Simplified filename format
        "ffmpeg_location": r"C:\Users\kmvis\Desktop\New folder\ffmpeg\bin\ffmpeg.exe",  # Custom FFmpeg path
        "ignoreerrors": True,  # Continue downloading even if one file fails
    }

    # Add format options based on download type
    if download_type == "audio":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    else:  # Default to video
        ydl_opts["format"] = "bestvideo+bestaudio/best"

    # Download using yt-dlp
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\n🚀 Starting download...")
            ydl.download([url])
        print("\n🎉 Download completed successfully!")
    except Exception as e:
        print(f"🚨 An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_content()
