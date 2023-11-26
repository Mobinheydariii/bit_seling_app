from django.db import models
from account.models import Singer, Producer



class Category(models.Model):
    # Category name, 100 characters maximum
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")
    
    # Category slug, 100 characters maximum, unique
    slug = models.SlugField(max_length=100, verbose_name="اسلاگ دسته بندی", unique=True)
    
    # Category image, upload to "categories/images/" directory
    image = models.ImageField(verbose_name="تصویر دسته بندی", upload_to="categories/images/")

    # Return category name when printed
    def __str__(self):
        return self.name

    # Define meta information for category model
    class Meta:
        verbose_name = "دسته بندی" # Category, singular
        verbose_name_plural = "دسته بندی ها" # Categories, plural
    

class Tag(models.Model):
    # name of the tag
    name = models.CharField(max_length=100, verbose_name="نام برچسب")

    # slug for tag (unique identifier)
    slug = models.SlugField(max_length=100, verbose_name="اسلاگ برچسب", unique=True)

    # return name as string representation of tag
    def __str__(self):
        return self.name

    # define metadata for tag model
    class Meta:
        # human-readable name of tag model
        verbose_name = "برچسب"

        # human-readable name of tag model (plural)
        verbose_name_plural = "برچسب ها"

class Track(models.Model):
    cat = models.ForeignKey(Category, 
                            on_delete=models.CASCADE, 
                            verbose_name="دسته بندی")
    
    singer = models.ForeignKey(Singer, 
                               on_delete=models.CASCADE, 
                               related_name='singer_tracks', verbose_name="خواننده")
    
    producer = models.ForeignKey(Producer,
                                 on_delete=models.SET_NULL, blank=True, null=True, 
                                 related_name="producer_traks", verbose_name="پرودوسر")
    
    title = models.CharField(max_length=200, 
                             verbose_name="عنوان ترک", unique=True)

    file = models.FileField(upload_to='music/', 
                            verbose_name="فایل موزیک", unique=True)
    
    description = models.TextField(blank=True, verbose_name="توضیحات ترک")

    release_date = models.DateField(verbose_name="تایم ریلیز شدن ترک")

    created = models.DateTimeField(auto_now_add=True, verbose_name="اضاقه شده")
    updated = models.DateTimeField(auto_now=True, verbose_name="آپدیت شده")

    tags = models.ManyToManyField(Tag, verbose_name="برچسب ها", blank=True)



    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['created']
        # human-readable name of track model
        verbose_name = 'ترک'
        # human-readable name of track model (plural)
        verbose_name_plural = 'ترک ها'

