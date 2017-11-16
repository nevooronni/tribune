from django.conf.urls import url#import url function
from . import views#import app views 
from django.conf import settings#import project setting from django.conf
from django.conf.urls.static import static#static function  

urlpatterns=[
	url('^$',views.news_today,name = 'newsToday'),#root page urlconfig
	url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),#capture our regex and send it to our view function 
	url(r'^search/',views.search_results,name='search_results'),
	url(r'^article/(\d+)',views.article,name='article')
]

if settings.DEBUG:#reference to the to the location to the uploaded files
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#To serve uploaded images on the dev serve we need to configure our url.py to register the media_root
