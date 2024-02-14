from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):

    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField('Description', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value 

    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'

    def __str__(self):
        return self.description
    

class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Bid Indicator')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value 

    class Meta:
        verbose_name = 'Bid Indicator'
        verbose_name_plural = 'Bids Indicator'

    def __str__(self):
        return f'Categoría Bid {self.category_product} : {self.discount_value}%' 
    

class Product(BaseModel):
    name = models.CharField('Product Name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product Description', blank=False, null=False)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Product Category', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value     
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    