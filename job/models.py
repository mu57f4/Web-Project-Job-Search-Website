from django.db import models
from users.models import User
from company.models import Company


class Job(models.Model):
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=0)
    description = models.TextField()
    requirements = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(max_length=30, choices=job_type_choices, null=True, blank=True)
    num_applicants = models.PositiveIntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.title
