from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")

    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + " " + self.last_name
