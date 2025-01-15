from django.shortcuts import render


def home(request):
    return render(request, template_name='leader_board/index.html', context={})


def leader_board(request):

    return render(request, template_name='leader_board/leader_board.html', context={})

def python_topic_1(request):
    return render(request, template_name='python_topics/intro.html', context={})
