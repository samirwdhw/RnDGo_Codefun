from django.shortcuts import render, redirect
from .forms import Post_data
# Create your views here.
def post_data(request):
	
	if request.method == "POST":

		form = Post_data(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.username = request.user.id
			post.save()
			return redirect('/home/')

	else:
		form = Post_data()

	return render(request, 'user_page.html', {'form':form})