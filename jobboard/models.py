from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User, Group

# Create your models here.

class Type(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Task(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    #job = models.ForeignKey('Operation', on_delete=models.SET_NULL, null=True) 
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the job")
    salary = models.TextField(max_length=1000, help_text="Enter how the fullfiled job will be rewarded")
    
    position = models.CharField('Location',max_length=1000,help_text='Set coordinates')
    
    #creation_date = models.DateField(Date.auto_now, null=True, blank=True)

    employer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    JOB_STATUS = (
        ('o', 'Open'),
        ('f', 'filled'),
    )

    status = models.CharField(max_length=1, choices=JOB_STATUS, blank=True, default='m', help_text='Job availability')
    '''
    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)  
    '''
    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.job.title)
#    @property
#    def is_overdue(self):
#        if self.due_back and date.today() > self.due_back:
#            return True
#        return False
        
class Operation(models.Model): 
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    summary= models.CharField(max_length=200)
    #salary = models.CharField(max_length=200)

    employer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.

    jtype = models.ManyToManyField(Type, help_text="Select the type of job")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    taskList = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book NOOOO!-instance.
        """
        return reverse('op-detail', args=[str(self.id)])
        #return self.title
    def display_type(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ jtype.name for jtype in self.jtype.all()[:3] ])
    display_type.short_description = 'Type'

        


class Employee(models.Model):
    """
    Model representing an author.
    """
    nickname = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('employee-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.nickname, self.organization) 