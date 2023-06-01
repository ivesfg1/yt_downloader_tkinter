from pytube import YouTube
from pathlib import Path

BASE_DIR = Path(__file__).parent / "downloads"


class YoutubeDownloader:
    @classmethod
    def generate_filename(cls, video_title, file_extension, output_path):
        #
        file_extension = file_extension.lower()
        filename = f"{video_title}.{file_extension}"

        number = 1
        while (output_path / filename).exists():
            filename = f"{video_title} ({number}).{file_extension}"
            number += 1

        return filename

    @classmethod
    def download_video(cls, video_url, file_extension="mp4"):
        #
        youtube_video = YouTube(video_url)
        output_path = BASE_DIR / "videos"

        video_title = youtube_video.title
        filename = cls.generate_filename(video_title, file_extension, output_path)

        youtube_video.streams.filter(
            file_extension=file_extension, progressive=True
        ).get_highest_resolution().download(output_path=output_path, filename=filename)


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    YoutubeDownloader.download_video(video_url)
