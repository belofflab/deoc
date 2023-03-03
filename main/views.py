from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from .models import Post

from telebot import TeleBot

BOT_TOKEN = '6190789151:AAGVZXiZZv19f6YrNl38Dj12f9HjG-7Grmc'
CHANNEL_ID = -1001791567557


bot = TeleBot(token=BOT_TOKEN, parse_mode='HTML')



def get_client_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
    ip = x_forwarded_for.split(',')[0]
  else:
    ip = request.META.get('REMOTE_ADDR')
  return ip


def is_ajax(request):
  return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
  posts = Post.objects.all().order_by('-date')[:3]
  return render(request, 'main/index.html', context={'posts':posts})

def about(request):
  return render(request, 'main/about.html', context={})

@csrf_exempt
def send_message(request):
  if is_ajax(request):
    dict_data = dict(request.POST)
    number = dict_data.get('number')[0]
    title = dict_data.get('title')[0]
    message = dict_data.get('message')[0]

    bot.send_message(chat_id=CHANNEL_ID, text=f"""
<b>Пришла заявка от пользователя:</b> {number}\n\n
<b>Суть проблемы:</b> {title}\n\n
<b>Услуга:</b> {message}    
""")
    return JsonResponse(data={"result":"success"})


class PostList(ListView):

  model = Post
  template_name = 'main/blog.html'

class PostDetail(DetailView):

  model = Post
  template_name = 'main/blog-detail.html'

def contact(request):
  return render(request, 'main/contact.html', context={})

def services(request):
  return render(request, 'main/services.html', context={})

def work(request):
  return render(request, 'main/work.html', context={})



def handler404(request, *args, **argv):
  return redirect('/')

def handler500(request, *args, **argv):
  return render(request, 'main/500.html', context={})

def handler403(request, *args, **argv):
  return render(request, 'main/403.html', context={})