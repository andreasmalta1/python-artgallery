import os
import webbrowser


class Art:
    """Stores information about works of Art in the Gallery"""

    ARTWORK = []

    def __init__(self, artist, title, url):
        self.artist = artist
        self.title = title
        self.url = url
        Art.ARTWORK.append(self)

    def show_image(self):
        url = "file://" + os.getcwd() + "/web/" + self.url
        webbrowser.open(url, new=2)
