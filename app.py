from pytube import YouTube


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(
            progressive=True, res="720p", file_extension="mp4"
        ).first()
        video.download(output_path)
        print("Download completed successfully")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    video_url = str(input("Link: "))
    output_directory = "DIRECTORY_NAME"
    download_video(video_url, output_directory)
