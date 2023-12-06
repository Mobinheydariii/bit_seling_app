from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from . import managers


class User(AbstractBaseUser, PermissionsMixin):

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

    username = models.CharField(max_length=20, 
                                 verbose_name="نام کاربری", unique=True, null=True)

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
    
    otp_auth = models.BooleanField(default=False, 
                                        verbose_name="احراض")

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = managers.UserManager()
    official = managers.OfficialManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['email', "username"]
    
    
    class Meta:
        ordering = ['type']
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"
        

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
            return self.is_admin

    def has_module_perms(self, app_label):
            return self.is_admin

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


class SimpleUserProfile(models.Model):
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, null=True)

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='users/', blank=True, null=True)

    full_name = models.CharField(verbose_name="نام کامل کاربر",
                                    max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}.....{self.full_name}"


    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"   
    


class Singer(User):

    objects = managers.SingerManager()
    official = managers.OfficialManager()


    class Meta:
        ordering = ['status']
        verbose_name = "خواننده"
        verbose_name_plural = "خوانندگان"

    def __str__(self):
        return self.artist_name


class SingerProfile(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True)

    artistic_name = models.CharField(max_length=200, 
                                     verbose_name="نام هنری", 
                                     unique=True, null=True, blank=True)

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='singer/image/profile/', blank=True, null=True)

    full_name = models.CharField(verbose_name="نام کامل کاربر",
                                    max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.singer.username}.....{self.full_name}"


    class Meta:
        verbose_name = "پروفایل خواننده"
        verbose_name_plural = "پروفایل خوانندگان"



class Producer(User):

    objects = managers.ProducerManager()
    official = managers.OfficialManager()


    class Meta:
        ordering = ['status']
        verbose_name = "پرودوسر"
        verbose_name_plural = "پرودوسر ها"

    def __str__(self):
        return self.artist_name
    

class ProducerProfile(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)

    artistic_name = models.CharField(max_length=200, 
                                     verbose_name="نام هنری", 
                                     unique=True, null=True, blank=True)

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='singer/image/profile/', blank=True, null=True)

    full_name = models.CharField(verbose_name="نام کامل کاربر",
                                    max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.producer.username}.....{self.full_name}"


    class Meta:
        verbose_name = "پروفایل پرودوسر"
        verbose_name_plural = "پروفایل پرودوسرها"

class Musician(User):

    objects = managers.MusicianManager()
    official = managers.OfficialManager()

    class Meta:
        ordering = ['status']
        verbose_name = "موزیسین"
        verbose_name_plural = "موزیسین ها"


    def __str__(self):
        return self.artist_name

class MusicianProfile(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True)

    artistic_name = models.CharField(max_length=200, 
                                     verbose_name="نام هنری", 
                                     unique=True, null=True, blank=True)

    bio = models.TextField(max_length=500, 
                           verbose_name="بیوگرافی", blank=True, null=True)
    
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='singer/image/profile/', blank=True, null=True)

    full_name = models.CharField(verbose_name="نام کامل کاربر",
                                    max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.musician.username}.....{self.full_name}"


    class Meta:
        verbose_name = "پروفایل موزیسین"
        verbose_name_plural = "پروفایل موزیسین ها"



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
    



class Otp(models.Model):
    
    user = models.OneToOneField(User,
                                verbose_name="کاربر",
                                on_delete=models.CASCADE, null=True)
    
    otp = models.IntegerField(verbose_name="کد اعتبار سنجی")
    
    token = models.CharField(max_length=100,
                             verbose_name="توکن", unique=True)
    

    class Meta:
        ordering = ['user']
        verbose_name = "otp"
        verbose_name_plural = "otp"

    def __str__(self):
        return self.email
    