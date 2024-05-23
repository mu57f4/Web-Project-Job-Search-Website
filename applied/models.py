from django.db import models
from users.models import User
from company.models import Company
from job.models import Job

class applied(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.user.username} applied to {self.job.title} at {self.company.name}'