from django.shortcuts import render, redirect
from django.utils import translation, timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Board
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# show board list
def board(request):
    boards = Board.objects.all()
    paginator = Paginator(boards, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = {'contacts': contacts, 'site': "board"}
    return render(request, 'board/board.html', context)

# show board 
def board_view(request, pk):
    board = Board.objects.get(pk=pk)
    board.lookup += 1
    board.save()
    context = {'board':board, 'site': "board"}
    return render(request, 'board/board_view.html', context)

# create board
def board_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        password = request.POST.get('password')
        post_type = request.POST.get('post_type')
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(
            author = author,
            password = password,
            post_type = post_type,
            title = title,
            content = content
        )
        board.save()
        context = {'board': board, 'site': "board"}
        return render(request,'board/board_view.html', context)

    return render(request, 'board/new_board.html')

# search board
def board_search(request):
    boards = Board.objects.all()
    post_type = request.GET.get('type')
    search = request.GET.get('search')
    page = request.GET.get('page')
    error = False
    
    if post_type != None:
        request.session['post_type'] = post_type
        request.session['search'] = search

    try:
        if request.session['post_type'] == "all":
            boards = boards.filter(title__icontains = request.session['search'])
        elif request.session['search'] == "":
            boards = boards.filter(post_type = request.session['post_type'])
        else:
            boards = boards.filter(post_type = request.session['post_type'], title__icontains = request.session['search'])
        paginator = Paginator(boards, 5) # Show 25 contacts per page
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    if boards.exists():
        message = "게시글을 찾았습니다."
    else:
        message = "해당 게시글이 없습니다."
        error = True
    context = {'boards':boards,'contacts': contacts, 'message':message, 'error':error, 'site': "board"}
    return render(request, 'board/board.html', context)

# update board 
def board_update(request):
    board = Board.objects.get(pk = request.POST.get('pk'))
    board.post_type = request.POST.get('post_type')
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.updated_at = timezone.now()
    board.save()

    context = {'board':board, 'site': "board"}
    return render(request,'board/board_view.html', context) 

# delete board
def board_delete(request, pk):
    board = Board.objects.get(pk = pk)
    board.delete()
    return redirect(reverse('board'))

def check_password(request):
    pk = request.POST.get('pk')
    password = request.POST.get('password')
    board = Board.objects.get(pk = pk)
    if password == board.password or str(password) == board.password:
        message = "인증되었습니다."
        print(message)
        url = request.POST.get('url')
        print(url)
        if url == "board/":
            print("성공했습니다.")
            return redirect("/board/delete/{}".format(pk))
    else:
        message = "Password error"
        url ='board/board_view.html'
    
    context = {'board':board, 'message':message, 'pk':pk}
    return render(request, url, context)
