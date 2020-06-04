from django.shortcuts import render
from . models import Album
from django.core.paginator import Paginator
# Create your views here.
def album(request):
    albums = Album.objects.all()
    albumspage = Album.objects.all()
    paginator = Paginator(albumspage, 3) #3개를 한 페이지로 자른다
    page = request.GET.get('page') #현재 페이지 정보를 가져온다
    posts = paginator.get_page(page)
    context = {'albums':albums, 'posts': posts}
    return render(request, 'album/album.html', context)
    