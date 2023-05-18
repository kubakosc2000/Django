from django.db import models

class Task(models.Model):
    TASK_TYPES = (
        ('regular', 'Zwykłe zadanie'),
        ('phone', 'Wykonać telefon'),
        ('email', 'Wysłać email'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.title
