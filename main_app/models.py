from django.db import models


# many-to-many relationship model
class NestMaterial(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name    


class Bird(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # make many-to-many association with NestMaterial
    nest_materials = models.ManyToManyField(NestMaterial)
    
    def __str__(self):
        return self.name


# one-to-many relationship model
class Sighting(models.Model):
    date = models.DateField('Date Seen')
    location = models.CharField(max_length=100)
    notes = models.TextField(max_length=300)

    # define relationship to Bird using foreign key
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sighting on {self.date}"

    class Meta:
        # sort by most recent date
        ordering = ['-date']


