from django.db import models

# Create your models here.
class Email(models.Model):
    """Модель для письма"""

    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    title = models.CharField(max_length=200)
    body = models.TextField()

    folder = models.CharField(max_length=20, default="inbox")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Возвращает строковое представление письма"""

        return self.title
    