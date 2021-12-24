import os
from yt_video.settings import CAPTIONS_DIR
from yt_video.settings import DOWNLOADS_DIR
from yt_video.settings import VIDEOS_DIR

class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.get_caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]   #  分割網址 只擷取右半部分

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT(' + str(self.id) + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id =' + str(self.id),
            'caption_filepath =' + str(self.get_caption_filepath),
            'video_filepath = ' + str(self.video_filepath)
        ])
        return '<YT(' + content + ')>'
