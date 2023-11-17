from django.db import models
from employers.models import EmployerProfile

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
    created_at = models.DateTimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employer = models.ForeignKey(
        EmployerProfile, on_delete=models.DO_NOTHING, default=None
    )

    def __str__(self):
        return(
            f"{self.job_title}"
            f"{self.employer}"
            f"({self.created_at:%d-%m-%Y})"
        )