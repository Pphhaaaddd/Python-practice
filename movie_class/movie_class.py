import webbrowser

class Movie():
    RATINGS = ['PG','G','R','PG-13']

    def __init__(self, title_, storyline_, poster_image_url_, trailer_youtube_url_):
        self.title = title_
        self.storyline = storyline_
        self.poster_image_url = poster_image_url_
        self.trailer_youtube_url = trailer_youtube_url_

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
