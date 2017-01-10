class Movie():
    """This class stores inforamtion about Movie object"""
    def __init__(self, title, storyline,  image, trailer):
        #Initialize class attributes
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
