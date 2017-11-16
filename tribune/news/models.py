from django.db import models#import models class configured to allow us to communicate with the db 
import datetime as dt

class Editor(models.Model):#created editor class inherits from model class 
	first_name = models.CharField(max_length = 30)#charfield  is the sql equivalent to varchar a string field for small to large size strings 
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 10,blank = True)

	def save_editor(self):
		self.save()

	def delete_editor(self):
		self.delete()

	#def display_all(self):
		#self.objects.all()

	#this updates our models so we can easily read it in the shell 
	def __str__(self):#string representation of our model
		return self.first_name
	class Meta:
		ordering = ['first_name']


class tags(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name 

class Article(models.Model):
	title = models.CharField(max_length = 60)
	post = models.TextField()#textarea tag in html
	editor = models.ForeignKey(Editor)#foreign key column defines one to many relationship to editor
	tags = models.ManyToManyField(tags)#many to many relationship with the tags class
	pub_date = models.DateTimeField(auto_now_add=True)#timestamp to establish when the articles were published 
	article_image = models.ImageField(upload_to = 'articles/')#image field takes upload_to argument defines where the image will be stored in the file system.
	#def save_article(self):
		#self.save()
	def __str__(self):
			return self.title		

	@classmethod
	def todays_news(cls):
		today = dt.date.today()#module to get todays date
		news = cls.objects.filter(pub_date__date = today)#qeury db to filter articles by current date 
		return news

	@classmethod
	def day_news(cls,date):#takes date object as an argument 
		news = cls.objects.filter(pub_date__date = date)
		return news

	@classmethod
	def search_by_title(cls,search_term):
		news = cls.objects.filter(title__icontains=search_term)#will filter our model data using the __icontains filter will check if any word in the title field of our articles matches the search_term 
		
		return news		
