
from django.shortcuts import render
from musician.models import Musician
from album.models import Album

# Create your views here.

def show_musicians_directory(request):
    dataAlbum = Album.objects.all()
    for i in dataAlbum:
        i.musician = Musician.objects.get(firstName = i.musician)
    return render(request,'show_musicians_directory.html',{'dataAlbum': dataAlbum})



