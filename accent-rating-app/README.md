# Accent Rating App

This project is designed to download a video from Google Drive, convert it to MP3, retrieve its transcript using Assembly AI, and rate the audio using Fluent. 

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

To set up the project, clone the repository and navigate to the project directory. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Download Video**: Ensure you have the Google Drive shareable link for the video you want to download.
2. **Run the Application**: Execute the main script to start the process:

```bash
python src/main.py
```

3. **Configuration**: You may need to set your API keys for Assembly AI and Fluent in the `main.py` file.

## Dependencies

The project requires the following Python libraries:

- `gdown`: For downloading files from Google Drive.
- `moviepy`: For converting video files to audio.
- `requests`: For making HTTP requests to APIs.
- `assemblyai`: For transcribing audio files.

## License

This project is licensed under the MIT License - see the LICENSE file for details.