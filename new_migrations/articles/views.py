from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from articles.models import TopicDetails
from articles.models import UserInfo
import json

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

def jsonify(obj):
	return {
		'topic': obj.topic,
	    'image': obj.image,
	    'date': str(obj.date),
	    'privacy': obj.privacy,
	    'details': obj.details,
		'handle': obj.handle.handle,
	};
def articles(request):
	ans = TopicDetails.objects.all()
	var = []
	for i in ans:
		var.append(jsonify(i))
	ans = json.dumps({
		'status': 'Success',
		'data': {
			'total_count': 5,
			'results': var
		}
	});
	# return render_to_response(ans)
	return HttpResponse(ans)
	# return render_to_response('articles.html', {'articles': TopicDetails.objects.filter(topic='NodeJS')})

def article(request, article_id = 1):
	category = 'NodeJS'
	return render_to_response('article.html', {'article': TopicDetails.objects.get(category=category)})
