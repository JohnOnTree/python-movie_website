# coding=utf-8
import webbrowser
class Movie():
    """电影类，封装有电影标题，描述，封面和预告片."""
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """初始化电影相关参数"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)