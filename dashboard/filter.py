import django_filters
from job.models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Job Keyword')
    class Meta:
        model = Job
        fields = ['title', 'years_of_experience', 'job_type']