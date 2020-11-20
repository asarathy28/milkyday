import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id= 'f842abb8ab18468daebfde0ba7d9ec04', client_secret= '24de10c8e2d74f468aba0ef17c5aac01')



#create spotify objecvt
#spotify:user:oc1oq9fqohjf9tez8tmr35fj4

class Music():

    def __init__(self):

        self.sp = spotipy.Spotify(auth_manager=auth_manager)

        self.user = 'oc1oq9fqohjf9tez8tmr35fj4'

        self.pl_name = []
        self.pl_id = []
        self.pl_image = []
        self.pl_description = []

        self.ns = self.sp.artist_albums('7FIqXqYZHMomTAcTXF4UHu',album_type=None, country='US', limit=1, offset=0)

        self.ns_name = self.ns['items'][0]['name']
        self.ns_image = self.ns['items'][0]['images'][0]['url']


        self.playlists = self.sp.user_playlists(self.user, limit=12, offset=0) #'1216336460'

        for i, t in enumerate(self.playlists['items']):
            self.pl_name.append(t['name'])
            self.pl_id.append(t['id'])
            self.pl_image.append(t['images'][0]['url'])
            self.pl_description.append(t['description'])

        self.albums = self.sp.artist_albums('7FIqXqYZHMomTAcTXF4UHu', album_type=('single','ablum'), country='US', limit=None, offset=0)

        self.album_name = []
        self.album_id = []
        self.album_image = []

        for i, t in enumerate(self.albums['items']):
            self.album_name.append(t['name'])
            self.album_id.append(t['id'])
            self.album_image.append(t['images'][0]['url'])





    def print_playlist (self):

        for i, name in enumerate(self.pl_name):
            id = self.pl_id[i]
            image = self.pl_image[i]
            description = self.pl_description[i]
            print(f"{name}, {id}, {description}, image link {image}")

    def print_ns (self):

        print(f"{self.ns_name}, {self.ns_image}")


    def print_albums (self):
        for i, name in enumerate(self.album_name):
            id = self.album_id[i]
            image = self.album_image[i]

            print(f"{name}, {id}, image link {image}")


#test = Music()

#test.print_ns()

#test.print_playlist()

#test.print_albums()



#print(json.dump(VAR, sort_key=True,indent=4))

#print(json.dumps(playlists, sort_keys=True, indent=4))
#print(insert_playlist())
