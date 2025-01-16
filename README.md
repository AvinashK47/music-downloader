# Song Downloader and Metadata Manager

A Python-based script to automate downloading songs from Spotify and YouTube while syncing their metadata (artist, album, track details). This tool utilizes open-source projects like **SpotDL**, **yt-dlp**, and **FFmpeg** for seamless music downloading and metadata management.

## **Project Overview**

After facing the challenge of rebuilding a **2000+ song** library after a phone reset, I created this script to automate:
- Fetching and downloading songs from Spotify and YouTube.
- Syncing metadata with the correct song information (artist, album, track).
- Simplifying the process of maintaining and updating a large music collection.

---

## **Features**

- **Extracts Spotify URLs**: Pulls valid Spotify links from text files.
- **Batch Downloads**: Downloads songs in chunks using SpotDL, yt-dlp, and FFmpeg for quality and performance.
- **Syncs Metadata**: Fetches and updates metadata from Spotify’s Web API (artist, album, title).
- **Search & Download**: Allows users to search for songs manually and choose to download.

---

## **Installation**

### **Prerequisites**

Before running the script, make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package installer)
- **Spotify API Credentials** (to fetch metadata)

### **For Arch Linux**

1. **Install Required Packages**
   First, ensure that Python, pip, FFmpeg, and required libraries are installed on your system:
   
   ```bash
   sudo pacman -S python python-pip ffmpeg
   ```

2. **Create a Python Virtual Environment**  
   It is recommended to create a virtual environment to manage dependencies:

   ```bash
   python -m venv song-downloader-env
   source song-downloader-env/bin/activate
   ```

3. **Install Dependencies**
   Install the required Python packages using `pip`:

   ```bash
   pip install spotdl yt-dlp spotipy
   ```

   - **SpotDL**: For downloading music from Spotify.
   - **yt-dlp**: For downloading music from YouTube.
   - **Spotipy**: Python library for accessing Spotify’s Web API.

4. **Obtain Spotify API Credentials**  
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create an application to get your `CLIENT_ID` and `CLIENT_SECRET`.
   - Add these credentials to your script or configure them in a `.env` file.

---

### **For Other Systems**

#### **Dependencies for Other Systems (Windows, macOS, etc.)**
1. **Install Python**:
   - Windows: Install [Python](https://www.python.org/downloads/).
   - macOS: Use `brew install python` if you have Homebrew.
   
2. **Install Required Libraries**:  
   Once Python is installed, use `pip` to install the dependencies:
   
   ```bash
   pip install spotdl yt-dlp spotipy
   ```

3. **Install FFmpeg**:
   - Windows: Download the [FFmpeg zip](https://ffmpeg.org/download.html) and add it to your PATH.
   - macOS: Use Homebrew to install:  
     ```bash
     brew install ffmpeg
     ```
   - Linux (Debian/Ubuntu-based):  
     ```bash
     sudo apt install ffmpeg
     ```

4. **Obtain Spotify API Credentials**:  
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new app and get the `CLIENT_ID` and `CLIENT_SECRET`.

---

## **Usage**

1. **Run the Script**:  
   Once the setup is complete, you can run the script directly from your terminal:

   ```bash
   python final.py
   ```

2. **Select an Option**:  
   The script will prompt you with options:
   - **1**: Extract Spotify links from a text file.
   - **2**: Process a text file for metadata.
   - **3**: Download songs in batches from a file of Spotify links.
   - **4**: Search and download a track manually.

3. **Provide Input Files**:  
   - For options 1 and 2, provide a text file with track names or links.
   - For batch downloads, provide a file with Spotify URLs.

---

## **Contributing**

I encourage contributions from anyone interested in improving or extending this project. Feel free to fork the repository and submit a pull request with any enhancements, bug fixes, or new features.

Here are some ideas for contributing:
- Improve platform compatibility for different operating systems.
- Enhance error handling and logging.
- Add additional features for playlist management.
- Create a GUI version of the script for easier use.

### **How to Contribute**

1. Fork the repository.
2. Clone your fork:
   
   ```bash
   git clone https://github.com/AvinashK47/music-downloader
   ```

3. Create a new branch for your changes:

   ```bash
   git checkout -b feature-name
   ```

4. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "Description of changes"
   ```

5. Push the changes to your fork:

   ```bash
   git push origin feature-name
   ```

6. Open a pull request in the original repository with a clear description of your changes.

---

## **Disclaimer**

- This script was developed for my system running **Arch Linux**. It may not work as expected on other operating systems.  
- If you encounter any issues, feel free to reach out—I’d be happy to help.  
- This is a quick solution to my problem, and it might not be polished for production use.  

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **At Last**

Feel free to contribute to this project! Whether you're adding features, fixing bugs, or improving the documentation, your help is appreciated. Let’s make this tool better for everyone!
