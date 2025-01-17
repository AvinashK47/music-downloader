import os
import re
import subprocess
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = ''  # Replace with your Spotify Client ID
CLIENT_SECRET = ''  # Replace with your Spotify Client Secret

# Initialize Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = Spotify(client_credentials_manager=client_credentials_manager)

# Function to extract Spotify links from a text file
def extract_spotify_links(input_file, output_file):
    spotify_url_pattern = r'https://open\.spotify\.com/track/[a-zA-Z0-9]+'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            links = re.findall(spotify_url_pattern, line)
            for link in links:
                outfile.write(link + '\n')
    print(f"Spotify links have been written to {output_file}")

# Function to search Spotify for a track
def search_spotify_for_track(track_name, artist_name):
    query = f"{track_name} {artist_name}"
    result = sp.search(q=query, type='track', limit=1)
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'spotify_url': track['external_urls']['spotify'],
            'album': track['album']['name']
        }
    return None

# Helper function to get song info from filename
def get_song_info_from_filename(filename):
    parts = filename.rsplit(' - ', 1)
    if len(parts) == 2:
        artist = parts[0].strip()
        track_name = parts[1].replace('.mp3', '').replace('.m4a', '').strip()
        return artist, track_name
    return None, None

# Process text file and fetch metadata for each song
def process_text_file(text_file, output_file):
    with open(output_file, 'w') as out_file, open(text_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split('. ', 1)
            if len(parts) == 2:
                filename = parts[1].strip()
                artist, track_name = get_song_info_from_filename(filename)
                if artist and track_name:
                    result = search_spotify_for_track(track_name, artist)
                    if result:
                        out_file.write(f"Found: {result['name']} by {result['artist']}\n")
                        out_file.write(f"Album: {result['album']}\n")
                        out_file.write(f"Spotify URL: {result['spotify_url']}\n")
                        out_file.write("-" * 40 + "\n")
                    else:
                        out_file.write(f"Could not find '{track_name}' by '{artist}' on Spotify.\n")
                        out_file.write("-" * 40 + "\n")
                else:
                    out_file.write(f"Skipping invalid file name: {filename}\n")
                    out_file.write("-" * 40 + "\n")

# Function to download a track using spotdl
def download_track(spotify_url):
    try:
        print(f"Downloading: {spotify_url}")
        subprocess.run(['spotdl', spotify_url], check=True)
        print("Download complete.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {spotify_url}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while downloading {spotify_url}: {e}")

# Function to download tracks in batches
def download_tracks_in_batches(input_file, batch_size=100):
    try:
        with open(input_file, 'r') as file:
            urls = [url.strip() for url in file.readlines()]
        total_urls = len(urls)
        for i in range(0, total_urls, batch_size):
            batch = urls[i:i + batch_size]
            print(f"Processing batch {i // batch_size + 1} with {len(batch)} links.")
            for url in batch:
                download_track(url)
            print(f"Batch {i // batch_size + 1} downloaded. Moving to the next batch...\n")
        print("Download complete for all tracks.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search and optionally download a track
def search_and_download():
    track_name = input("Enter the track name: ").strip()
    artist_name = input("Enter the artist name (optional, press Enter to skip): ").strip()
    result = search_spotify_for_track(track_name, artist_name)
    if result:
        print(f"Found: {result['name']} by {result['artist']}")
        print(f"Album: {result['album']}")
        print(f"Spotify URL: {result['spotify_url']}")
        download_choice = input("Do you want to download this track? (yes/no): ").strip().lower()
        if download_choice == 'yes':
            download_track(result['spotify_url'])
        else:
            print("Skipping download.")
    else:
        print("Track not found on Spotify.")

# Main function
def main():
    print("Welcome to the Spotify/Youtube Song Downloader!")
    print("Choose an option:")
    print("1. Extract Spotify links from a file")
    print("2. Process a text file for metadata")
    print("3. Download songs in batches")
    print("4. Search and download a track")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == '1':
        input_file = input("Enter the path to the input file: ").strip()
        output_file = input("Enter the path to the output file: ").strip()
        extract_spotify_links(input_file, output_file)
    elif choice == '2':
        text_file = input("Enter the path to the text file with song details: ").strip()
        output_file = input("Enter the path for the output text file: ").strip()
        process_text_file(text_file, output_file)
    elif choice == '3':
        input_file = input("Enter the path to the file with Spotify links: ").strip()
        download_tracks_in_batches(input_file)
    elif choice == '4':
        search_and_download()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
