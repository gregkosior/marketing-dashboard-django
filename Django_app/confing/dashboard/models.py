
from django.db import models

class ShopData(models.Model):
	ad_group = models.CharField(max_length=255)
	month = models.CharField(max_length=20)
	impressions = models.IntegerField()
	clicks = models.IntegerField()
	ctr = models.FloatField()
	conversions = models.IntegerField()
	conv_rate = models.FloatField()
	cost = models.FloatField()
	cpc = models.FloatField()
	revenue = models.FloatField()
	sale_amount = models.FloatField()
	pandl = models.FloatField()

	def __str__(self):
		return f"{self.ad_group} ({self.month})"
