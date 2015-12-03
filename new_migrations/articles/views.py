from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from articles.models import Article

# Create your views here.

def hello(request):
	name = 'revs'
	html = '<html><body>Hi %s. Awesome !</body></html>' %name
	return HttpResponse(html)

def hello_template(request):
	name = 'revs';
	t = get_template('hello.html');
	html = t.render(Context({'name': name}))
	return HttpResponse(html)

def hello_easy_way(request):
	name = 'revs'
	return render_to_response('hello.html', {'name': name})

def articles(request):
	return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id = 1):
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})