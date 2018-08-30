import webbrowser
# imports webbrowser in order to allow access to the web


class Movie( ):
# creating a class called called Movie

    # within the movie class, created a funtion to create space in memory (init)
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    # function to open website trailers in a new browser 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
