from django.db import models

class Authors(models.Model):
    full_name = models.CharField()
    age = models.PositiveBigIntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Books(models.Model):
    name = models.CharField()
    ganre = models.CharField()
    price = models.DecimalField(decimal_places=1)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    caption = models.TextField()
    picture = models.ImageField()
    publisher = models.CharField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    book_name = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_name = models.CharField()
    user_phone = models.PositiveBigIntegerField(max_length=12)
    order_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

