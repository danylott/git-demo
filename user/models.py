from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(...)

    def __str__(self) -> str:
        return self.name

    def say_hi(self) -> str:
        if self.age < 18:
            return f"Hi, {self.name}"

        return f"Hello, {self.name}"
