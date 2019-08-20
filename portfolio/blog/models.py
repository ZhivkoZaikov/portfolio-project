from django.db import models
import random
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    # The summary and pub_date_pretty functions are for testing purposes and they are not used in this app
    # I have used other functions instead (yay)
    # check python strftime for more information about the letters and their meaning
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def prety_slug(self):
        return self.slug.lower()
