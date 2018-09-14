import webbrowser
class Video():
    def __init__(self , movie_title , movie_duration):
        self.title = movie_title
        self.duration = movie_duration
class Movie(Video):
    def __init__(self,movie_title,movie_duration,movie_storyline,poster_image,trailer_youtube):
        Video.__init__(self , movie_title , movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
class TvShow():
    def __init__(self,movie_title, movie_duration , season , episode , tv_station):
        Video.__init__(self , movie_title , movie_duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
    def het_local_listing(self):
        pass
