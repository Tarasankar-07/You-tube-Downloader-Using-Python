from pytube import YouTube

def download_youtube_video(video_url, save_path):
    try:
        yt = YouTube(video_url)

        video_stream = yt.streams.get_highest_resolution()

        video_stream.download(save_path)
        
        print(f"Video downloaded successfully and saved to {save_path}")
    
    except Exception as e:

        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    # example
    video_url = "Enter YouTube video URL"
    
    save_path = "Enter Save path location"
    
    download_youtube_video(video_url, save_path)


