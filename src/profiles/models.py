from django.db import models

# Create your models here.

#V03
class UserProfile(models.Model):
    user_name = models.CharField(max_length=25, default="JDoe")
    image = models.FileField(upload_to="tempdata")

    def __repr__(self):
        return f"pk={self.id} user_name={self.user_name} image_path={self.image}"
