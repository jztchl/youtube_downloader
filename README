# 🎬 YouTube Downloader with yt-dlp

A simple and user-friendly Python script to download videos or audio files from YouTube, including playlist support. You can choose to download either the video or audio from a YouTube playlist or single video URL, and customize the quality of the download.

## Features

* Download individual videos or full playlists
* Choose between downloading videos or audio files
* Customize the quality of the video and audio downloads
* Customizable output folder for saving downloaded files
* Graceful error handling: continues downloading even if one file fails
* Automatically uses your specified FFmpeg path for audio processing
* Simple setup with `yt-dlp`

## Requirements

* Python 3.6+
* `yt-dlp` (for downloading videos and audio)
* FFmpeg (for audio extraction)

## Installation

### Install Dependencies

1. Install yt-dlp:
   ```bash
   pip install yt-dlp
   ```

2. Download and Install FFmpeg:
   * Download FFmpeg from the [official website](https://ffmpeg.org/download.html)
   * Extract and note the path to `ffmpeg.exe`
   * For Windows, ensure that the path to `ffmpeg.exe` is set correctly in the script (`ffmpeg_location`)

## Setup Instructions

1. Clone the repository or create the script manually

2. Download FFmpeg:
   * Install FFmpeg and note down the path to `ffmpeg.exe`
   * Update the script with the correct FFmpeg path:
     ```python
     "ffmpeg_location": r"C:\path\to\ffmpeg\bin\ffmpeg.exe",
     ```

3. Ensure the FFmpeg folder path for `ffmpeg_location` exists or modify the path in the script

## Usage

### Running the Script

1. Open a terminal or command prompt
2. Navigate to the script's directory
3. Run the script:
   ```bash
   python download.py
   ```

### Script Prompts

The script will ask for the following information:

* **YouTube URL**: A valid YouTube playlist or video URL
* **Save Location**: Folder to save files (current directory by default)
* **Download Type**: Choose between:
  * `audio`: Downloads MP3 audio only
  * `video`: Downloads video with audio (default)
* **Video Quality**: For video downloads (`best`, `worst`, `720p`, `1080p`, etc.)
* **Audio Quality**: For audio downloads (`best`, `192k`, `128k`, etc.)

### Example Usage

```
Enter the YouTube playlist or video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the folder to save files (or press Enter for the current directory): downloads
Do you want to download 'video' or 'audio' only? (video/audio, default is video):
What video quality do you want? (best, worst, or 1080p, 720p, etc., default is best):
What audio quality do you want? (best, 192k, 128k, etc., default is best):
```

### Example Output

**Single Video Download**:
```
🎉 Download completed successfully!
File saved as: downloads/Rick Astley - Never Gonna Give You Up.mp4
```

**Playlist Download**:
```
🎉 Download completed successfully!
Files saved in: downloads/
- Song 1.mp4
- Song 2.mp4
- Song 3.mp4
```

**Error Handling**:
```
🚨 An error occurred: Some error message here.
🎉 Download completed successfully!
```

## Error Handling

* Failed downloads are skipped, allowing the script to continue with remaining items
* Error messages are displayed in the console for troubleshooting

## Customization

* **FFmpeg Path**: Modify the `ffmpeg_location` field in the script
* **Output Template**: File naming format (`%title%-%id%.%(ext)s`) can be changed in the `outtmpl` field
* **Video Quality**: Adjust the `quality` parameter (`best`, `worst`, `1080p`, `720p`)
* **Audio Quality**: Modify the `preferredquality` parameter (`best`, `192k`, `128k`)
