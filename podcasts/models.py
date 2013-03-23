from django.db import models

class Channel(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length = 500)
	link = models.URLField()
	copyright = models.CharField(max_length = 200)
	webmaster = models.EmailField()
	itunes_image = models.URLField()
	itunes_author = models.EmailField()
	itunes_owner_name = models.CharField(max_length=50)
	itunes_owner_email = models.EmailField()
	itunes_explicit = models.BooleanField()
	itunes_category = models.CharField(max_length=100)
	itunes_subtitle = models.CharField(max_length=200)
	itunes_summary = models.CharField(max_length=700)
	language = models.CharField(max_length=20)
	def __unicode__(self):
		return self.title

class Episode(models.Model):
	channel = models.ForeignKey(Channel)
	title = models.CharField(max_length=200)
	link = models.URLField()
	description = models.CharField(max_length=500)
	enclosure_url = models.URLField()
	enclosure_length = models.IntegerField()
	guid = models.URLField()
	category = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	itunes_author = models.EmailField()
	itumes_keywords = models.CharField(max_length=100)
	itunes_image = models.URLField()
	def __unicode__(self):
		return self.title
