from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # кредит доверия к юзеру
    karma = models.IntegerField(default=0)
    # пройдена ли модерация (имя, фамилия, аватар)
    # сбрасывается при изменении одной из этих трех полей
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StudyClass(models.Model):
    year = models.IntegerField(default=1)
    letter = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f'{self.year}{self.letter}'

    class Meta:
        ordering = ['year', 'letter']


class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.name}'


class Student(models.Model):
    study_class = models.ForeignKey(StudyClass, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.profile}'


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student} - {self.subject.name}'

    class Meta:
        unique_together = ['student', 'subject']

