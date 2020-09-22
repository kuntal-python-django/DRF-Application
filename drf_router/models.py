from django.db import models
from django.contrib.auth.models import User

# OneToOne
class UserDetail(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'UserDetail'
        managed = True
        verbose_name = 'UserDetail'
        verbose_name_plural = 'UserDetails'


# ForeignKey
class Post(models.Model):
    content = models.CharField(max_length=10)

    def __str__(self):
        return self.content


class Comment(models.Model):
    name = models.CharField(max_length=10)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comment_realtion',
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name