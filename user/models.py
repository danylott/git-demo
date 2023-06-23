from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.last_name + " " + self.name

    def say_hi(self) -> str:
        # age < 18 Hi, self.name
        # age >= 18 Hi, self.name self.last_name
        return f"Hi, {self.name}"
