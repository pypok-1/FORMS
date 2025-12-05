from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    """Модель категорії."""

    title = models.CharField(max_length=180, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=["title"])]

    def __str__(self) -> str:
        return str(self.title)


class Post(models.Model):
    """Модель поста."""

    author = models.ForeignKey(  # ForeignKey - у одного автора можеь быть много постов (Один до багатьох)
        UserModel, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') # domashka

    def __str__(self):
        return f"{self.title} by {self.author.username}"

# domashka


class Profile(models.Model):
    User = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, related_name='profile'
    )
    name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=30, null=False)
    bio = models.TextField(max_length=1000)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    likes = models.ManyToMany(Profile,
                              on_delete=models.CASCADE,
                              related_name='liked_by')
    def __str__(self):
        return f'name : {self.name}, last name : {self.last_name}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField(max_length=1000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self):
        return f'{self.post}'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'