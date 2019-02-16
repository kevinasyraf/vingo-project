from django.shortcuts import render

def about(request):
	context = {
		'judul' : 'About',
		'banner' : 'about/img/banner_about.png',
		'subjudul' : 'This website was made by Kevin Asyraf from Class E Foundation of Programming 1 to fulfill Programming Task 4'
	}
	return render(request, 'about.html', context)
