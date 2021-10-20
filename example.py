from py_bandcamp import BandCamp, BandcampAlbum, BandcampTrack

url = "https://deadunicorn.bandcamp.com/track/astronaut-problems"
track = BandcampTrack.from_url(url)
print(track.duration)
print(track.data)
print(track.artist.data)
print(track.album.data)
print(BandCamp.get_stream_url(url))
print(track.album.featured_track.stream)
print(track.stream)

album = BandcampAlbum.from_url("https://naxatras.bandcamp.com/album/iii")
print(album.data)
print(album.artist)
print(album.releases)
print(album.comments)
print([t.data for t in album.tracks])

tag_list = BandCamp.tags()
tags = BandCamp.search_tag('black-metal')
albums = BandCamp.search_albums('black-metal')
tracks = BandCamp.search_tracks('astronaut problems')
labels = BandCamp.search_labels("black")
artists = BandCamp.search_artists('Planet of the Dead')

url = "https://perturbator.bandcamp.com/music"
# TODO parse these urls also
