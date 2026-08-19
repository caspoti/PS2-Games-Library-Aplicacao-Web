from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(blank=True,null=True)
    rating = models.IntegerField(
        default=1,
        choices=[
            (1, "★☆☆☆☆"),
            (2, "★★☆☆☆"),
            (3, "★★★☆☆"),
            (4, "★★★★☆"),
            (5, "★★★★★"),
        ]
    )
    review = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ps2/',blank=False,null=True)
    trailer_link = models.CharField(max_length=200, default='') #só o codigo do video no fim do link do youtube - ex: K8Sxmr4yhJ0

    def __str__(self):
        return self.title

