from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name = "نام سایت")
    site_url = models.CharField(max_length=400, verbose_name = "ادرس سایت")
    site_logo = models.ImageField(upload_to= "images/main_logo", verbose_name = "لوگو صفحه اصلی سایت")
    address = models.CharField(max_length= 400, verbose_name = "ادرس")
    phone = models.CharField(max_length= 200 ,verbose_name = "تلفن")
    copyright_text = models.TextField(verbose_name = "متن کپی رایت")
    about_us_text = models.TextField(verbose_name = "متن درباره ما")
    about_us_page_logo = models.ImageField(upload_to = "images/about_us_logo", verbose_name = "لوگو صفحه درباره ما")
    email = models.EmailField(null= True, blank = True ,verbose_name = "ایمیل سایت")
    is_main_setting = models.BooleanField(default = False, verbose_name = "تنظیمات فعال")

    def __str__(self):
        return f"{self.site_name}"

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات سایت"

class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name = "عنوان")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دسته بندی لینک های فوتر"
        verbose_name_plural = "دسته بندی های لینک های فوتر"

class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name = "عنوان")
    url = models.URLField(verbose_name="ادرس لینک")
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete = models.CASCADE , verbose_name = "دسته بندی لینک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک های فوتر"



class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name = "عنوان اسلایدر")
    button_url = models.URLField(max_length=400, verbose_name = "ادرس لینک")
    image = models.ImageField(upload_to = "images/sliders")
    short_description = models.TextField(verbose_name = "توضیحات اسلایدر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "تمامی اسلایدر ها"

class Banner(models.Model):
    class BannerPositions(models.TextChoices):
        product_list = 'product_list', 'صفحه لیس محصولات'
        product_detail = 'product_detail', 'صفحه جزییات محصولات'
        about_us = 'about_us', 'صفحه درباره ما'
        contact_us = 'contact_us', 'صفحه تماس با ما'


    title = models.CharField(max_length=200, verbose_name="عنوان بنر")
    url = models.URLField(max_length=400, verbose_name="ادرس بنر")
    image = models.ImageField(upload_to="images/banners", verbose_name="تصویر بنر")
    position = models.CharField(verbose_name="محل قرار گیری بنر", choices=BannerPositions.choices, max_length=200)
