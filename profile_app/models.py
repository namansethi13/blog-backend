from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
