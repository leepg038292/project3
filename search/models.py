from django.db import models

# Create your models here.
# search/models.py

class Item(models.Model):
    Brand = models.CharField(max_length=255)  # 항목 이름
    Price = models.DecimalField(max_digits=10, decimal_places=2)          # 가격
    Gender = models.CharField(max_length=255)  # 성별
    P_name = models.TextField() # 한글 향수 이름
    Name = models.TextField()  # 영어 향수 이름
    Rate = models.DecimalField(max_digits=10, decimal_places=2) # 평점
    Winter = models.DecimalField(max_digits=10, decimal_places=2)
    Spring = models.DecimalField(max_digits=10, decimal_places=2)
    Summer = models.DecimalField(max_digits=10, decimal_places=2)
    Fall = models.DecimalField(max_digits=10, decimal_places=2)
    season = models.TextField()
    Day = models.DecimalField(max_digits=10, decimal_places=2)
    Night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    Main_Components = models.TextField()
    Top_Notes = models.TextField() 
    Middle_Notes = models.TextField()
    Base_Notes = models.TextField()
    Longetivity = models.TextField()
    Image = models.TextField()
    Skint_ype = models.TextField()
    Style = models.TextField()
    MBTI = models.TextField()

    

    def __str__(self):
        return self.Name