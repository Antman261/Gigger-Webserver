from django.db import models

# Create your models here.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True, db_column="AuthorID")
    first_name = models.CharField(max_length=255, db_column="FirstName")
    last_name = models.CharField(max_length=255, db_column="LastName")
    twitter = models.CharField(max_length=250, blank=True, db_column="Twitter")
    bio = models.TextField(blank=True, db_column="Bio")
    profile_picture_url = models.CharField(max_length=255, blank=True, db_column="ProfilePictureUrl")
    created = models.DateTimeField(auto_now_add=True, db_column="AuthorCreated")
    edited = models.DateTimeField(blank=True, auto_now=True, db_column="AuthorEdited")

    class Meta:
        db_table="tblAuthor"
        managed = False

    def __str__(self):
        return self.first_name +" "+ self.last_name


class BlogPost(models.Model):
    blog_post_id = models.AutoField(primary_key=True, db_column="BlogPostID")
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column="AuthorID")
    title = models.CharField(max_length=255, db_column='Title')
    url_slug = models.SlugField(db_column='UrlSlug')
    image_url = models.CharField(max_length=255, db_column='ImageUrl')
    content = models.TextField(db_column='Content')
    short_description = models.CharField(max_length=255, db_column='ShortDescription')
    created = models.DateTimeField(auto_now_add=True, db_column='BlogPostCreated')
    edited = models.DateTimeField(blank=True, auto_now=True, db_column='BlogPostEdited')

    class Meta:
        ordering = ["-created"]
        db_table="tblBlogPost"
        managed = False

    def __str__(self):
        return self.title
