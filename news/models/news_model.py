from django.db import models
from news.models.user_model import Users
from news.models.category_model import Categories
from news.models.validators import validate_title


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, validators=[validate_title]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Categories, null=False)

    def __str__(self):
        return self.title
