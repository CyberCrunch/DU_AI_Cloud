from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import economy, military, humans
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

#from .forms import RenewBookForm

#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy

def overview(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_quanta=economy.quanta #.objects.all().count()
    #num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'main_map.html',
        context={'num_quanta':num_quanta,'num_visits':num_visits},
                #'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            #'num_visits':num_visits}, # num_visits appended
    )
    
    
    
    

class economyView(generic.ListView):
    model = economy

'''    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
'''        
class militaryView(generic.DetailView): #prev book detail
    model = military
    

class humansView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = humans
    #template_name ='catalog/bookinstance_list_borrowed_user.html'
    #paginate_by = 10
    
    #def get_queryset(self):
    #    return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
        
'''    
@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
'''