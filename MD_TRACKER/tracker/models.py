from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    floor = models.IntegerField()

    def __str__(self):
        return self.name + " Piętro " + str(self.floor)
    

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.producer
    


class Usage(models.Model):
    use_from = models.DateTimeField()
    use_to = models.DateTimeField()
    user = models.CharField(max_length=30)
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    
    # storage = models.ForeignKey(Room,on_delete=models.CASCADE)