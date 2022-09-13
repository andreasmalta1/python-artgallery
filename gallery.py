from product import Art
from web import art_gallery

art1 = Art("Joan White", "Barcelona Afternoon", "images/01.jpg")
art2 = Art("John Dusseldorf", "Lemon & Lime", "images/02.jpg")
art3 = Art("Lucy Pattersfield", "Change of Scene", "images/03.jpg")
art4 = Art("Patrick McGee", "Into the Blue", "images/04.jpg")
art5 = Art("Joe Trumpton", "Feeling Yellow", "images/05.jpg")
art6 = Art("Amerigo Fernandez", "The Fancy of Industry", "images/06.jpg")
art7 = Art("Cristoff Bergmann", "90 Degrees of Yellow", "images/07.jpg")

art_gallery.open_gallery_page(Art.ARTWORK)
