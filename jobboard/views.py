from django.shortcuts import render
from django.views import generic
from .models import Employee, Type, JobTemplate, JobInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import CreateJobForm

# Create your views here.

def jobboard(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_jobs=JobTemplate.objects.all().count()
    num_jinstances=JobInstance.objects.all().count()
    # Available books (status = 'a')
    num_jinstances_filled=JobInstance.objects.filter(status__exact='f').count()
    num_employees =Employee.objects.count()  # The 'all()' is implied by default.
 
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'jobboard.html',
        context={'num_jobs':num_jobs,'num_jinstances':num_jinstances,
            'num_jinstances_filled':num_jinstances_filled,'num_employees':num_employees,
            'num_visits':num_visits}, # num_visits appended
    )
    
    
    
    

class JobListView(generic.ListView):
    model = JobTemplate

'''    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
'''        
class JobDetailView(generic.DetailView):
    model = JobTemplate
    
class EmployeeListView(generic.ListView):
    model = Employee
class EmployeeDetailView(generic.DetailView):
    model = Employee
        
class FilledJobsListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = JobInstance
    template_name ='jobboard/jobinstance_list_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return JobInstance.objects.filter(employer=self.request.user).filter(status__exact='o').order_by('employer')
        
    
def CreateJobView(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    #job_form=get_object_or_404(JobInstance, pk = pk)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateJobForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            #book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('job-board') )

    # If this is a GET (or any other method) create the default form.
    else:
        job_title = "default-error"
        form = CreateJobForm(initial={'job_title': proposed_renewal_date,})

    return render(request, 'jobboard/.html', {'form': form, 'jobinst':job_inst})
  
        
#@permission_required('catalog.can_mark_returned')
def Create_Project_Legate(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    job_inst=get_object_or_404(JobInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateJobForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            #book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('job-board') )

    # If this is a GET (or any other method) create the default form.
    else:
        job_title = "default-error"
        form = CreateJobForm(initial={'job_title': proposed_renewal_date,})

    return render(request, 'jobboard/.html', {'form': form, 'jobinst':job_inst})
  