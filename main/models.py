from profile import Profile

from django.db import models

# Create your models here.
from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories, blank=True, null=true')
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False



class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})

class Image(models.Model):
    image =  models.ImageField(upload_to='posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


    def __str__(self):
        return self.image.url

#comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('published', )

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
