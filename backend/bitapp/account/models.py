from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import(
    UserManager,
    SingerManager,
    ProducerManager,
    SupporterManager,
    SimpleUserManager, 
)



class User(AbstractBaseUser):

    class Types(models.TextChoices):
        SIMPLE_USER = "SU", "Simple_user" # The person who wants to listen or download music
        SINGER = "SI", "Singer" # The person who wants to buy bits
        PRODUCER = "PR", "Producer" # The person who wants to sell bits
        MUSICIAN = "MU", "Musician" # The person who wants to sell and buy bits
        SUPORTER = "SP", "Supporter" # The person who listen to bits and  Accepts the bits

    
    type = models.CharField(
        max_length=2, 
        choices=Types.choices,
        default=Types.SIMPLE_USER,
    )

    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=255,
        unique=True,
    )

    phone = models.CharField(verbose_name="شماره تلفن",
                                   max_length=11, unique=True)
    
    
    f_name = models.CharField(verbose_name="نام",
                              max_length=200, null=True)
    
    l_name = models.CharField(verbose_name="نام خانوادگی",
                              max_length=200, null=True)
    
    
    is_active = models.BooleanField(default=True,
                                    verbose_name="فعال")
    
    is_admin = models.BooleanField(default=False,
                                   verbose_name="ادمین")

    date_joined = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = "artist_name"
    REQUIRED_FIELDS = ['email', 'phone', 'type']
    
    
    class Meta:
        ordering = ['type']
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"
        

    def __str__(self):
        return self.artist_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    


    


class SimpleUser(User):
    objects = SimpleUserManager()


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SIMPLE_USER
        return super().save(*args, **kwargs)
    
    


class Singer(User):

    class UserStatus(models.TextChoices):
        OFIFICIAL = "OFL", "Official"
        UN_OFFICIAL = "UFL", "Un_Official"

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    status = models.CharField(
        max_length=3,
        verbose_name="وضعیت کاربر", 
        choices=UserStatus.choices, 
        default=UserStatus.UN_OFFICIAL,
    )

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    

    objects = SingerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SINGER
        return super().save(*args, **kwargs)

    


class Producer(User):

    class UserStatus(models.TextChoices):
        OFIFICIAL = "OFL", "Official"
        UN_OFFICIAL = "UFL", "Un_Official"

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    
    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    status = models.CharField(
        max_length=3,
        verbose_name="وضعیت کاربر", 
        choices=UserStatus.choices, 
        default=UserStatus.UN_OFFICIAL,
    )

    persentage = models.IntegerField(verbose_name="سهم پرودوسر",
                                     validators=[MinValueValidator(80),
                                               MaxValueValidator(100)], help_text="سهم پرودوسر از فروش بیت بین 80 تا 100 درصد می باشد")

    objects = ProducerManager()


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PRODUCER
        return super().save(*args, **kwargs)
    


class MusicianManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MUSICIAN)
    


class Musician(User):

    class UserStatus(models.TextChoices):
        OFIFICIAL = "OFL", "Official"
        UN_OFFICIAL = "UFL", "Un_Official"

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    
    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    status = models.CharField(
        max_length=3,
        verbose_name="وضعیت کاربر", 
        choices=UserStatus.choices, 
        default=UserStatus.UN_OFFICIAL,
    )

    persentage = models.IntegerField(verbose_name="سهم موزیسین",
                                     validators=[MinValueValidator(80),
                                               MaxValueValidator(100)], help_text="سهم موزیسین از فروش بیت بین 80 تا 100 درصد می باشد")

    objects = MusicianManager()


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.MUSICIAN
        return super().save(*args, **kwargs)

    


class Supporter(User):
    Supporter_id = models.CharField(max_length=20, 
                                    verbose_name="آیدی پشتیبان", unique=True)

    objects = SupporterManager()


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SUPORTER
        return super().save(*args, **kwargs)