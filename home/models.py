from django.db import models


#pass-om123
#makemigrations- create changes and save in a file
#migrate-apply the pending changes created by make migrations

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_paid = models.BooleanField(default=False)
    github_url = models.URLField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='project_pdfs/', blank=True, null=True)
