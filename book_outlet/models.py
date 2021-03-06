from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_name()
        
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"\nTitle: {self.title} \nAuthor: {self.author.first_name} {self.author.last_name}\n\n"