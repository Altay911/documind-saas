from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    # This links the PDF to the specific user who uploaded it
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # the name of the file
    title = models.CharField(max_length=255)

    # This tells Django to save the physical file into a folder called 'user_pdfs'
    uploaded_file = models.FileField(upload_to='user_pdfs/')

    # Automatically records the exact time it was uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class APIUsage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    queries_today = models.IntegerField(default=0)
    last_query_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.queries_today} queries"