from django.db import models

class JobOffer(models.Model):
    JOB_TYPE_CHOICES = (
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Becario', 'Becario'),
        ('Temporal', 'Temporal'),
        ('Contrato', 'Contrato'),
    )

    job_title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)