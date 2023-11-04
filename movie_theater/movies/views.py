from django.shortcuts import render, redirect

import json
import datetime
# Create your views here.

# Homepage
def home(request):
    page_title = "Home Page"
    return render(request, 'movies/home.html',
                  context={'page_title': page_title})

# Cookies Check
def cookies(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
           print(request.COOKIES['visit_nbr'])
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "movies/cookies.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr,
   max_age=datetime.timedelta(seconds=10), samesite="LAX")
   return response

from .movie_forms import MovieForm
# Django Form
def create(request):
    dico_data = request.COOKIES
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            entry = []
            
            response = render(request, "movies/add_success.html",)
            response.set_cookie(samesite="LAX", key="movieData", value=json.dumps(
            {'id_movie': request.POST['movie'],
            'id_year': request.POST['year'],
            'id_actors': request.POST['actors']}))
        return response
    else:
        form = MovieForm()
    return render(request, "movies/create.html", {'movie_form': form})

# Forms Helper
# def formsHelper(request):
#    dico_data = request.COOKIES
#    id = dico_data
#    print(dico_data)
#    if 'id' in dico_data:
#        id += 1
#    else:
#        id = 1
#    return str(id)
