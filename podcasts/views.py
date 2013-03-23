from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from podcasts.models import Channel

def rss(request, channel_id):
	channel = get_object_or_404(Channel, pk=channel_id)
	return render(request, 'podcasts/rss.xml',{'channel':channel})