from django.contrib import admin
from .models import Editor,Article,tags

class ArticleAdmin(admin.ModelAdmin):#inherits from the model admin
	filter_horizontal = ('tags',)#filter horizontal property that allows ordering of many to many fiels and pass in the tags article field.

#models
admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)#pass in the sublass as a second argument 
admin.site.register(tags)
