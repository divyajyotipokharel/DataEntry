from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    file_no = models.CharField(max_length=400)
    record_no = models.CharField(max_length=400)
    entry_date = models.CharField(max_length=400)
    ref_no = models.CharField(max_length=400)
    invoice_no = models.CharField(max_length=400)
    courier_name = models.CharField(max_length=400)
    con_no = models.CharField(max_length=400)
    dispatch_date = models.CharField(max_length=400)
    dispatch_by = models.CharField(max_length=400)
    sales_date = models.CharField(max_length=400)
    sales_time = models.CharField(max_length=400)
    customer_name = models.CharField(max_length=400)
    mail_address = models.CharField(max_length=400)
    agent_name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    state = models.CharField(max_length=400)
    zip_code = models.CharField(max_length=400)
    customer_phone = models.CharField(max_length=400)
    credit_card_type = models.CharField(max_length=400)
    credit_card_number = models.CharField(max_length=400)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.record_no