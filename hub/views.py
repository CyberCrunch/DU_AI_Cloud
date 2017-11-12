from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index1.html',
        context={}, # num_visits appended
    )