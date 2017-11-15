from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

	#set up method
	def setUp(self):#create an instance of the Editro class before every test
		self.james = Editor(first_name = 'James',last_name = 'Muriuki',email = 'james@moringaschool.com')

	#test instance to confirm that the object is being instantiated correctly 
	def test_instance(self):
		self.assertTrue(isinstance(self.james,Editor))

	#test save method
	def test_save_method(self):
		self.james.save_editor()#save our instance object
		editors = Editor.objects.all()#list out all of our objects from our db
		self.assertTrue(len(editors) > 0)#confrims if our objects has been added to our db

	#test to see if you can delete 
	def test_delete_method(self):
		self.james.save_editor()
		self.james.delete_editor()
		editors = Editor.objects.all()
		self.assertTrue(len(editors) == 0)

	#def test_display_method(self):
		#self.jame.save_editor()
		#editors = Editor.objects.all()

class ArticleTestClass(TestCase):

	#set up method
	def setUp(self):
		self.fees = Article(title = 'SCHOOL FEES',post = 'pay school feers on time.')
		self.james = Editor(first_name = 'James',last_name = 'Muriuki',email = 'james@moringaschool.com')
		self.james.save_editor()

		#creating a new tag and saving it
		self.new_tag = tags(name = 'testing')
		self.new_tag.save()		

		self.new_article = Article(title = 'Test Article',post = 'This is a random test post',editor = self.james)#equate editor instance that we created and saved.
		self.new_article.save()

		self.new_article.tags.add(self.new_tag)#many to many relationship

	def tearDown(self):
		Editor.objects.all().delete()
		tags.objects.all().delete()
		Article.objects.all().delete()

	def test_get_news_today(self):
		today_news = Article.todays_news()
		self.assertTrue(len(today_news) > 0)

	def test_get_news_by_date(self):
		test_date = '2017-03-17'
		date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
		news_by_date = Article.day_news(date)
		self.assertTrue(len(news_by_date) == 0)#since there was no news posted on that day we expect it to return an empty string 

	#test if istance is istantianted propertly
	#def test_instance(self):
		#self.assertTrue(isinstance(self.fees,Article))	

	#test save method 
	#def test_save_method(self):
		#self.fees.save_article()
		#articles = Article.objects.all()
		#self.assertTrue(len(articles) > 0)

	#test delete method
	#def test_delete_method(self):
		#self.fees.save_article()
		#self.fees.delete_article()
		#articles = Article.objects.all()
		#self.assertTrue(len(articles) == 0)





