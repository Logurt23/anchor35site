from django.shortcuts import render

# redirect to a url...
from django.http import HttpResponseRedirect

# Not uses yet...
def homepage(request):
    render(request, 'index.html', {})