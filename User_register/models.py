from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # To delete profile on deletion of a user but not vice versa. It also ensures that one user has one profile.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')   # To add profile picture of the user.


    def _str_(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)    # for overriding model's save method in Django
        img = Image.open(self.image.path)   # will open the image of a specified size that we want to be.
        if img.height>500 and img.width>500:  # if size of image is more then 500 pixels then resize it. To reduce files system space and also improve speed of the website.
            size = (500, 500)
            img.thumbnail(size)
            img.save(self.image.path)
