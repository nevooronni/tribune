from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,Http404#import the httpresponse class from the django.http module reposible for returning reponse to the user.
import datetime as dt
from .models import Article

#deleted the date function since all of that is now defined with the date filter

def news_today(request):
	date = dt.date.today()
	news = Article.todays_news()
	return render(request,'all-news/today-news.html',{"date":date,"news":news})#pass in 3 arguments last one is a dictionary of values that we want to pass into the template the dictionary is referred to as the context in django

def past_days_news(request,past_date):

	try:
		# Converts data from the string Url
		date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
		
	except ValueError:
		#Raise 404 error when ValueError is thrown
		raise Http404()
		assert False 

	if date == dt.date.today():
		return redirect(news_today)

	news = Article.day_news(date)
	return render(request,'all-news/past-news.html',{"date":date,"news":news})

def search_results(request):

	if 'article' in request.GET and request.GET["article"]:#we first check if the article query exists in our request.GET object
		search_term = request.GET.get("article")#get the search term using the request.GET object
		searched_articles = Article.search_by_title(search_term)#search the user input
		message = f"{search_term}"

		return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})

	else:
		message = "You haven't searched for any term"
		return render(request,'all-news/search.html',{"message":message})

def article(request,article_id):#pass in artitcle id from url 
	try:
		article = Article.objects.get(id = article_id)#query db for article
	except DoesNotExist:#catch the does not exist expection when we fail to find object with the id and throw a 404 error 
		raise Http404()
	return render(request,"all-news/article.html",{"article":article})	