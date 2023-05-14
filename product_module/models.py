from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', null= True, blank= True, on_delete= models.CASCADE)
    title = models.CharField(max_length=200, verbose_name= "عنوان")
    url_title = models.CharField(max_length=300, verbose_name= "عنوان در url")
    is_active = models.BooleanField(default=True, verbose_name= "فعال/ غیر فعال")
    is_delete = models.BooleanField(default=True, verbose_name = "حذف شده/نشده")
    

    def __str__(self):
        return f"{self.title} - {self.url_title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام محصول")
    slug = models.SlugField(max_length=400, null=False, db_index=True, unique=True, allow_unicode=True, verbose_name="نام در url (با حروف لاتین و با خط فاصله نوشته شود)")
    price = models.IntegerField(verbose_name="قیمت به ریال")
    quntity = models.IntegerField(verbose_name="تعداد در انبار")
    short_description = models.CharField(verbose_name="توضیحات کوتاه", max_length=400)
    description = models.TextField(verbose_name="توضیحات اصلی")
    product_barcode = models.IntegerField(verbose_name="بارکد کالا")
    is_active = models.BooleanField(default=True, verbose_name="فعال /غیرفعال")
    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / نشده")

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
