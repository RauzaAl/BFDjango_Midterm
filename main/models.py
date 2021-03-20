from django.db import models
from django.utils import timezone


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True


class Book(BookJournalBase):
    GENRE_CHOICES = (
        (1, "horror"),
        (2, "drama"),
        (3, "fantasy")
    )
    genre = models.PositiveIntegerField(choices=GENRE_CHOICES, null=True)
    num_pages = models.IntegerField()


class Journal(BookJournalBase):
    TYPE_CHOICES = (
        (1, "Bullet"),
        (2, "Food"),
        (3, "Travel"),
        (4, "Sport")
    )
    type = models.PositiveIntegerField(choices=TYPE_CHOICES, null=True)
    publisher = models.CharField(max_length=100)

