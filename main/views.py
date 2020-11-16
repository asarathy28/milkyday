from django.shortcuts import render
from .milky_spotify import Music

# Create your views here.
def home(request):

    myMusic = Music()

    new_single = {'name':myMusic.ns_name, 'image':myMusic.ns_image}
    playlists = zip(myMusic.pl_name, myMusic.pl_id, myMusic.pl_image)

    return render(request, "main/home.html", {'new_single':new_single, 'playlists':playlists})

def music(request):
    myMusic = Music()
    #'1216336460'

    #playlists = {'name':myMusic.pl_name, 'id':myMusic.pl_id, 'image':myMusic.pl_image}
    albums = zip(myMusic.album_name, myMusic.album_id, myMusic.album_image)

    return render(request, "main/music.html", {'albums':albums})

def portfolio(request):

    return render(request, "main/portfolio.html", {})
