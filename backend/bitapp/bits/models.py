from django.db import models
from django.urls import reverse
# Create your models here.


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



class AcceptedManger(models.Manager):
    """Custom manager for accepted records."""

    def get_queryset(self):
        """Filter records based on the 'accepted' status."""
        return super().get_queryset().filter(status=Bit.Status.ACCEPTED)


class DraftManger(models.Manager):
    # Returns queryset of draft status
    def get_queryset(self):
        return super().get_queryset().filter(status=Bit.Status.DRAFT)
    

class Bit(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        ACCEPTED = 'َAC', 'Accepted'
        REJECTED = 'RJ', 'Rejected'

    # Represents the title of the Bit
    title = models.CharField(max_length=200, verbose_name="تایتل بیت", unique=True)

    # Represents the URL slug for the Bit
    slug = models.SlugField(max_length=200, verbose_name="اسلاگ(url)", unique=True)

    # Represents the beats per minute (BPM) of the Bit
    bpm = models.BigIntegerField(verbose_name="")

    # Represents the musical keys of the Bit
    keys = models.CharField(max_length=2)

    # Represents the publish date of the Bit
    publish = models.DateField(verbose_name="زمان انتشار", blank=True, null=True)

    # Represents the created date of the Bit
    created = models.DateTimeField(auto_now_add=True)

    # Represents the updated date of the Bit
    updated = models.DateTimeField(auto_now=True)

    # Represents the image of the Bit
    image = models.ImageField(verbose_name="تصویر بیت", upload_to="bits/images/image/")

    # Represents the free mp3 file of the Bit
    mp3_free = models.FileField(verbose_name="mp3 رایگان", upload_to='bits/files/mp3/free/')

    # Represents the premium mp3 file of the Bit
    mp3_no_tag_in = models.FileField(verbose_name="pm3 پولی", upload_to='bits/files/mp3/no_tag/')

    # Represents the wav file of the Bit
    wav = models.FileField(verbose_name="فایل wav", upload_to='bits/files/wav/')

    # Represents the status of the Bit
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DRAFT)

    # Represents the total plays of the Bit
    plays = models.IntegerField(verbose_name="تعداد پلی", default=0)

    # Represents the total likes of the Bit
    likes = models.IntegerField(verbose_name="تعداد لایک", default=0)

    # Represents the total dislikes of the Bit
    dislikes = models.IntegerField(verbose_name="تعداد dislike ها", default=0)

    # Represents the total comments of the Bit
    comments = models.IntegerField(verbose_name="تعداد کامنت ها", default=0)

    # Managers for the Bit model
    objects = models.Manager() 
    accepted = AcceptedManger() 
    drafts = DraftManger() 

    class Meta:
        verbose_name = "بیت"
        verbose_name_plural = "بیت ها"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bits:detail', args=[self.slug])

    def increment_plays(self):
        self.plays += 1
        self.save()

    def increment_likes(self):
        self.likes += 1
        self.save()

    def increment_dislikes(self):
        self.dislikes += 1
        self.save()

    def increment_comments(self):
        self.comments += 1
        self.save()
