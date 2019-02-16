from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'Home',
		'banner' : 'img/banner_home.png',
		'subjudul' : 'Welcome to VINGO! Please log in if you have already signed up in VINGO'
	}
	return render(request, 'home.html', context)