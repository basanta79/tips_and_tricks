import json
import xml.etree.ElementTree as et


class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:

    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    @staticmethod
    def _serialize_to_json(song):
        payload = dict(
            id=song.song_id,
            title=song.title,
            artist=song.artist
        )
        return payload

    @staticmethod
    def _serialize_to_xml(song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

song1 = Song('1', "titulo1", "artista1")
song2 = Song('2', "titulo2", "artista2")
song3 = Song('3', "titulo3", "artista3")

serializer = SongSerializer()

print(serializer.serialize(song1, 'JSON'))

print(serializer.serialize(song1, 'XML'))
