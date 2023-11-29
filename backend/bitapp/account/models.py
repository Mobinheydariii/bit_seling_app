from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from . import managers


class User(AbstractBaseUser):

    class Types(models.TextChoices):
        SIMPLE_USER = "SU", "Simple_user" # The person who wants to listen or download music
        SINGER = "SI", "Singer" # The person who wants to buy bits
        PRODUCER = "PR", "Producer" # The person who wants to sell bits
        MUSICIAN = "MU", "Musician" # The person who wants to sell and buy bits
        SUPORTER = "SP", "Supporter" # The person who listen to bits and  Accepts the bits

    
    class UserStatus(models.TextChoices):
        """
        Enum class for user statuses.
        """
        OFFICIAL = "OFL", "Official"
        UN_OFFICIAL = "UFL", "Un_Official"


    type = models.CharField(
        max_length=2, 
        choices=Types.choices,
    )

    status = models.CharField(
        max_length=3,
        verbose_name="وضعیت کاربر", 
        choices=UserStatus.choices, 
        default=UserStatus.UN_OFFICIAL,
    )

    

    user_name = models.CharField(max_length=20, 
                                 verbose_name="نام کاربری", unique=True)

    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=255,
        unique=True,
    )

    phone = models.CharField(verbose_name="شماره تلفن",
                                   max_length=11, unique=True)
    
    is_active = models.BooleanField(default=True,
                                    verbose_name="فعال")
    
    is_admin = models.BooleanField(default=False,
                                   verbose_name="ادمین")

    date_joined = models.DateTimeField(auto_now_add=True)

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='users/', blank=True, null=True)

    f_name = models.CharField(verbose_name="نام",
                              max_length=200, null=True, blank=True)
    
    l_name = models.CharField(verbose_name="نام خانوادگی",
                              max_length=200, null=True, blank=True)

    objects = managers.UserManager()
    official = managers.OfficialManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ['email', "phone"]
    
    
    class Meta:
        ordering = ['type']
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"
        

    def __str__(self):
        return self.user_name

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

    objects = managers.SimpleUserManager()
    official = managers.OfficialManager()

    class Meta:
        verbose_name = "کاربر ساده"
        verbose_name_plural = "کاربران ساده"
    
    


class Singer(User):

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    

    objects = managers.SingerManager()
    official = managers.OfficialManager()


    class Meta:
        ordering = ['status']
        verbose_name = "خواننده"
        verbose_name_plural = "خوانندگان"

    def __str__(self):
        return self.artist_name


class Producer(User):

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    
    persentage = models.IntegerField(verbose_name="سهم پرودوسر",
                                     default=80, validators=[MinValueValidator(80),
                                                                MaxValueValidator(100)],
                                                                help_text="سهم پرودوسر از فروش بیت بین 80 تا 100 درصد می باشد")

    objects = managers.ProducerManager()
    official = managers.OfficialManager()


    class Meta:
        ordering = ['status']
        verbose_name = "پرودوسر"
        verbose_name_plural = "پرودوسر ها"

    def __str__(self):
        return self.artist_name
    


class Musician(User):

    artist_name = models.CharField(max_length=30, 
                                   verbose_name="نام هنری", unique=True)
    
    persentage = models.IntegerField(verbose_name="سهم موزیسین",
                                     default=80, validators=[MinValueValidator(80),
                                                                MaxValueValidator(100)],
                                                                help_text="سهم موزیسین از فروش بیت بین 80 تا 100 درصد می باشد")

    objects = managers.MusicianManager()
    official = managers.OfficialManager()

    class Meta:
        ordering = ['status']
        verbose_name = "موزیسین"
        verbose_name_plural = "موزیسین ها"


    def __str__(self):
        return self.artist_name



class Supporter(User):

    supporter_id = models.CharField(max_length=20, 
                                    verbose_name="آیدی پشتیبان", unique=True, null=True, blank=True)
    
    supporter_password = models.CharField(max_length=16,
                                          verbose_name="رمز عبور پشتیبان", null=True, blank=True)

    objects = managers.SupporterManager()
    official = managers.OfficialManager()
    

    class Meta:
        ordering = ['supporter_id']
        verbose_name = "پشتیبان"
        verbose_name_plural = "پشتیبان ها"


    def __str__(self):
        return self.supporter_id