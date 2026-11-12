from django.db import models

class Authors(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Books(models.Model):
    name = models.CharField(max_length=100)
    ganre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100)
    picture = models.ImageField(upload_to="images/")
    publisher = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    book_name = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=12)
    order_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

