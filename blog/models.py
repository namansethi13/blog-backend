from django.db import models
from PIL import Image
from core.utils import compress_and_rename_image
from django.utils.text import slugify 

section_choices = [
    ("title" , "Title"),
    ("raw_content" , "Raw Content"),
    ("image" , "Image"),
    ("footer" , "Footer"),
]

class Post(models.Model):
    title = models.TextField()
    created_date = models.DateField(auto_now=True)
    description = models.TextField(default="no description available")
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.created_date}"
    

class Section(models.Model):
    section_title = models.TextField(blank=True, null=True)
    section_type = models.CharField(choices=section_choices, max_length=20)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/blog_pictures", blank=True, null=True)
    alt_text = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post,related_name="sections", on_delete=models.CASCADE)
    order = models.IntegerField()

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        has_changed = False

        if not is_new and self.pk:
            try:
                old_image = Section.objects.get(pk=self.pk).image
                if old_image != self.image:
                    has_changed = True
                    old_image.delete(save=False)
            except Section.DoesNotExist:
                has_changed = True
        
        else:
            has_changed = True
        
        if has_changed and self.image:
            self.image = compress_and_rename_image(self.image, partial_name=slugify(f"{self.alt_text or self.post.title}_"))

        
        super().save(*args , **kwargs)

        if has_changed and old_image and old_image.name and old_image.storage.exists(old_image.name):
            old_image.delete(save=False)

    def delete(self, *args, **kwargs):
        if self.image and self.image.name and self.image.storage.exists(self.image.name):
            self.image.delete(save=False)
        super().delete(*args, **kwargs)


    def __str__(self):
        return f"#{self.order} = {self.post.title} - {self.section_type}"
    

