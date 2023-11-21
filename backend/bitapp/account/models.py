from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator





class UserManager(BaseUserManager):
    def create_user(self , user_name, email , phone, password = None): 
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        email  = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 

    def create_superuser(self, user_name, email, phone, password=None):
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        user = self.create_user(
            email=self.normalize_email(email),
            user_name=user_name,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class  SimpleUserManager(models.Manager):
    def create_user(self , user_name, email , phone, password = None): 
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        email  = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SIMPLE_USER)
    

class SingerManager(models.Manager):
    def create_user(self , user_name, email , phone, password = None): 
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        email  = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SINGER)
    

class ProducerManager(models.Manager):
    def create_user(self , user_name, email , phone, password = None): 
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        email  = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PRODUCER)
    

class SupporterManager(models.Manager):
    def create_user(self , user_name, email , phone, password = None): 
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        if not email or len(email) <= 0 :  
            raise  ValueError("Email field is required !") 
        
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        email  = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SUPPORTER)



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

    user_name = models.CharField(max_length=20, 
                                 verbose_name="نام کاربری", unique=True)

    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=255,
        unique=True,
    )

    phone = models.CharField(verbose_name="شماره تلفن",
                                   max_length=11, unique=True)
    
    image = models.ImageField(verbose_name="تصویر پروفایل", 
                              upload_to='users/', blank=True, null=True)

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