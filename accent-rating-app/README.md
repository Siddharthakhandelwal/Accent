# Accent Rating App

This project is designed to download a video from Google Drive, convert it to WAV, retrieve its transcript using Assembly AI, and rate the audio using Fluent. 

## Project Structure

```
accent-rating-app
├── src
│   ├── main.py          # Main script to orchestrate the process
│   └── utils
│       └── __init__.py  # Utility functions for the project
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Installation

### 1. Python Dependencies

To set up the project, clone the repository and navigate to the project directory. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 2. FFmpeg Installation

This application requires FFmpeg to be installed on your system and available in your PATH.

#### Windows
1. Download FFmpeg from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) (recommended: "ffmpeg-git-full" build)
2. Extract the ZIP file to a location on your computer (e.g., `C:\ffmpeg`)
3. Add the `bin` folder to your system PATH:
   - Right-click on "This PC" or "My Computer" and select "Properties"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System variables", find and select the "Path" variable, then click "Edit"
   - Click "New" and add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`)
   - Click "OK" on all dialogs to save the changes

#### macOS
Using Homebrew:
```bash
brew install ffmpeg
```

#### Linux
Using apt (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

Using yum (CentOS/RHEL):
```bash
sudo yum install ffmpeg ffmpeg-devel
```

## Usage

1. **Download Video**: Ensure you have the Google Drive shareable link for the video you want to download.
2. **Run the Application**: Execute the main script to start the process:

```bash
python src/main.py
```

3. **Configuration**: You may need to set your API keys for Assembly AI and Fluent in the `main.py` file.

## Dependencies

The project requires the following:

### Python Libraries
- `gdown`: For downloading files from Google Drive.
- `moviepy`: For video processing.
- `requests`: For making HTTP requests to APIs.
- `assemblyai`: For transcribing audio files.
- `ffmpeg-python`: Python wrapper for FFmpeg.

### System Dependencies
- `FFmpeg`: Required for audio/video processing.

## License

This project is licensed under the MIT License - see the LICENSE file for details.