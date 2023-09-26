from datetime import datetime

class Photo:
    def __init__(self, name):
        self.name = name
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Photo: {self.name} taken at {self.timestamp}"

class PhotoAlbum:
    def __init__(self):
        self.photos = []

    def take_photo(self, name):
        photo = Photo(name)
        self.photos.append(photo)
        return photo

    def save(self):
        return AlbumMemento(self.photos)

    def restore(self, memento):
        self.photos = memento.get_saved_photos()

    def show_photos(self):
        print("Photo Album:")
        for photo in self.photos:
            print(photo)

class AlbumMemento:
    def __init__(self, photos):
        self.saved_photos = photos

    def get_saved_photos(self):
        return self.saved_photos

# Uso del patrón Memento
album = PhotoAlbum()

# Tomar fotos
photo1 = album.take_photo("Foto 1")
photo2 = album.take_photo("Foto 2")
photo3 = album.take_photo("Foto 3")

album.show_photos()

# Guardar el estado actual del álbum
memento = album.save()

# Tomar más fotos
photo4 = album.take_photo("Foto 4")
photo5 = album.take_photo("Foto 5")

album.show_photos()

# Restaurar el estado anterior del álbum
album.restore(memento)

album.show_photos()