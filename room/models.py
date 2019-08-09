from django.db import models

class Room(models.Model):
    ROOM_CHOICE = {
        ('원룸','원룸'),
        ('투룸','투룸'),
        ('아파트','아파트'),
        ('고시텔','고시텔'),
        ('오피스텔','오피스텔')
    }


    title = models.CharField(max_length=300)
    roomtype = models.CharField(max_length=100, choices=ROOM_CHOICE)
    price = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published', null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    phonenumber = models.IntegerField()
    description = models.TextField()
    mainimg = models.ImageField(upload_to='images/', blank=True)
    img1 = models.ImageField(upload_to='images/', blank=True)
    img2 = models.ImageField(upload_to='images/', blank=True)
    img3 = models.ImageField(upload_to='images/', blank=True)
    sample5_address = models.CharField(max_length=300,null=True)


    def __str__(self):
        return self.title
