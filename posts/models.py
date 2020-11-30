#Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model. """
    
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    profile = models.ForeignKey('users.Profile',on_delete=models.CASCADE) #para no hascer referencia circulares 'user.Profile'
    
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    
    crated = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return f'{self.title} by @{self.user.username}'




# from django.db import models

# class User(models.Model):

#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     is_admin = models.BooleanField(default=False)

#     bio = models.TextField(blank=True)

#     birthdate = models.DateField(blank=True,null=True)

#     country = models.CharField(max_length=100,null=True)
#     city = models.CharField(max_length=100,null=True)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.email