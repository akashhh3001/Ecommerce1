from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.product_name
    @property
    def offer_price(self):
        Offs=Offers.objects.filter(product=self)
        if Offs:
            off=Offs[0]
            return self.price - off.discount
        else:
            return self.price
        
    @property
    def p_reviews(self):
        qs=Reviews.objects.filter(product=self)
        return qs
    
    def avg_rating(self):
        qs=self.p_reviews
        if qs:
            total=sum([r.rating for r in qs])
            return total/len(qs)
        else:
            return 0
        

class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)


class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curdate=datetime.date.today()
    expDate=curdate+datetime.timedelta(days=5)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=260,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment
    
        



class Offers(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    discount=models.CharField(max_length=12)
    isAvailable=models.BooleanField(default=True)
    start_date=models.DateField(default=datetime.date.today,null=True)
    end_date=models.DateField(default=datetime.date.today,null=True)
    




