from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=300)
    roomtype = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    phonenumber = models.IntegerField()
    description = models.TextField()
    mainimg = models.ImageField(upload_to='images/')
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    

