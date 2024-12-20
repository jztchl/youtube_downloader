
```markdown
# 🎬 YouTube Downloader with yt-dlp

A simple and user-friendly Python script to download videos or audio files from YouTube, including playlist support. You can choose to download either the video or audio from a YouTube playlist or single video URL, and customize the quality of the download.

## Features
- Download individual videos or full playlists.
- Choose between downloading videos or audio files.
- Customize the quality of the video and audio downloads.
- Customizable output folder for saving downloaded files.
- Graceful error handling: continues downloading even if one file fails.
- Automatically uses your specified FFmpeg path for audio processing.
- Simple setup with `yt-dlp`.

## Requirements
- Python 3.6+
- `yt-dlp` (for downloading videos and audio)
- FFmpeg (for audio extraction)
  
### Install Dependencies:
1. **Install yt-dlp**:
   ```bash
   pip install yt-dlp
   ```

2. **Download and Install FFmpeg**:
   - FFmpeg is required for audio extraction. Download FFmpeg from the official website:
     - [FFmpeg Downloads](https://ffmpeg.org/download.html)
   - After downloading, extract and make note of the path to `ffmpeg.exe`.
   - **For Windows**, ensure that the path to `ffmpeg.exe` is set correctly in the script (`ffmpeg_location`).
   - Alternatively, if you want to install FFmpeg using `pip`:
     ```bash
     pip install imageio[ffmpeg]
     ```

## Setup Instructions
1. **Clone the repository or create the script manually**.
2. **Download FFmpeg**:
   - Make sure you have FFmpeg installed and note down the path to `ffmpeg.exe`.
   - Update the script with the correct path to FFmpeg:
     ```python
     "ffmpeg_location": r"C:\path\to\ffmpeg\bin\ffmpeg.exe",
     ```

3. **Ensure the following folder exists** or you can change the path inside the script:
   - FFmpeg folder path for `ffmpeg_location`.

## Usage

### Running the Script:
1. Open a terminal or command prompt.
2. Navigate to the folder where the script is located.
3. Run the script:
   ```bash
   python download.py
   ```

### Script Prompts:
- **YouTube URL**: Provide a valid YouTube playlist or video URL.
- **Folder to Save Files**: Specify the folder where the files should be saved. Leave blank to use the current directory.
- **Download Type**: Choose whether to download the video or audio:
   - **audio**: Downloads only the audio in MP3 format.
   - **video**: Downloads the video with both video and audio.
   - If you skip this prompt, it defaults to video.
- **Video Quality**: If downloading a video, choose the video quality (e.g., `best`, `worst`, or specify resolution like `720p`, `1080p`).
- **Audio Quality**: If downloading audio, choose the quality (e.g., `best`, `192k`, `128k`).

Example Input:
```
Enter the YouTube playlist or video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the folder to save files (or press Enter for the current directory): downloads
Do you want to download 'video' or 'audio' only? (video/audio, default is video):
What video quality do you want? (best, worst, or 1080p, 720p, etc., default is best):
What audio quality do you want? (best, 192k, 128k, etc., default is best):
```

### Example Output:
- **Single Video Download**:
  ```
  🎉 Download completed successfully!
  File saved as: downloads/Rick Astley - Never Gonna Give You Up.mp4
  ```

- **Playlist Download**:
  ```
  🎉 Download completed successfully!
  Files saved in: downloads/
  - Song 1.mp4
  - Song 2.mp4
  - Song 3.mp4
  ```

- **Graceful Error Handling**:
  ```
  🚨 An error occurred: Some error message here.
  🎉 Download completed successfully!
  ```

## Error Handling
- The script will skip any failed downloads (e.g., if a video is unavailable) and continue with the rest of the playlist or video downloads.
- Errors are printed to the console for troubleshooting.

## Customization
- **FFmpeg Path**: You can customize the FFmpeg path in the `ffmpeg_location` field in the script.
- **Output Template**: The file names follow the format `%title%-%id%.%(ext)s`. You can modify this in the `outtmpl` field if you want to change how the files are named.
- **Video Quality**: Modify the `quality` parameter to change the video quality (`best`, `worst`, or a specific resolution like `1080p`, `720p`).
- **Audio Quality**: Modify the `preferredquality` parameter to change the audio quality (`best`, `192k`, `128k`, etc.).

---

Feel free to fork this repo or modify it to suit your needs. Enjoy downloading your favorite YouTube content with the quality you prefer! 🚀
```

---
