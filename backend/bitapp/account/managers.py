from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager
from . import models



class OfficialManager(Manager):
    def get_queryset(self, *args, **kwargs):
        # Return queryset of only oficial Users
        return super().get_queryset(*args, **kwargs).filter(status=models.User.UserStatus.OFFICIAL)



class UserManager(BaseUserManager):
    # Method to create user with provided credentials
    def create_user(self , user_name, email , phone, password = None): 
        # Validate username
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        # Validate phone number
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        # Validate email
        if not email or len(email) <= 0 :  
            raise ValueError("Email field is required !") 
        # Validate password
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        # Create user
        email = email.lower() 
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 

    # Method to create superuser with provided credentials
    def create_superuser(self, user_name, email, phone, password=None):
        # Validate username
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        # Validate phone number
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        # Validate email
        if not email or len(email) <= 0 :  
            raise ValueError("Email field is required !") 
        # Validate password
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
    


class SimpleUserManager(Manager):
    def create_user(self, user_name, email, phone, password=None): 
        # Validate required fields
        if not user_name or len(user_name) <= 0:
            raise ValueError("Users must have a valid username")

        if not phone or len(phone) <= 0:
            raise ValueError('Phone number is required ')

        if not email or len(email) <= 0:   
            raise ValueError("Email field is required !")

        if not password or len(password) < 8:
            raise ValueError("Password should be at least 8 characters long ")

        # Set user properties
        email = email.lower()
        user = self.model(
            user_name = user_name,
            email = email,
            phone = phone
        )
        user.set_password(password) 
        user.save(using = self._db) 
        return user 

    def get_queryset(self, *args, **kwargs):
        # Return queryset of Simple User type only
        return super().get_queryset(*args, **kwargs).filter(type=models.User.Types.SIMPLE_USER)
    

class SingerManager(Manager):
    # create singer user
    def create_user(self, user_name, email, phone, password=None):
        # validate user_name
        if not user_name or len(user_name) <= 0:
            raise ValueError("Users must have a valid username")

        # validate phone
        if not phone or len(phone) <= 0:
            raise ValueError('Phone number is required')

        # validate email
        if not email or len(email) <= 0:
            raise ValueError("Email field is required")

        # validate password
        if not password or len(password) < 8:
            raise ValueError("Password should be at least 8 characters long")

        # lowercase email
        email = email.lower()

        # create singer user
        user = self.model(
            user_name=user_name,
            email=email,
            phone=phone
        )

        # set password
        user.set_password(password)

        # save user
        user.save(using=self._db)

        # return user
        return user

    # get singer queryset
    # def get_queryset(self, *args, **kwargs):
    #     return super().get_queryset(*args, **kwargs).filter(User.Types.SINGER)
    

class ProducerManager(Manager):
    # Method to create producer user
    def create_user(self , user_name, email , phone, password = None): 
        # Validate username
        if not user_name or len(user_name) <= 0 :
            raise ValueError("Users must have a valid username")
        
        # Validate phone number
        if not phone or len(phone) <= 0 :
            raise ValueError('Phone number is required ')
        
        # Validate email field
        if not email or len(email) <= 0 :  
            raise ValueError("Email field is required !") 
        
        # Validate password
        if not password or len(password) < 8 :
            raise ValueError("Password should be at least 8 characters long ")
        
        # Set email to lowercase
        email = email.lower() 
        
        # Create producer user
        user = self.model( 
            user_name = user_name,
            email = email,
            phone = phone
        ) 
        
        # Set password and save user
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
    
    # Method to get queryset for producer users
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=models.User.Types.PRODUCER)


class MusicianManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=models.User.Types.MUSICIAN)


class SupporterManager(Manager):
    # Method to create supporter user
    def create_user(self, user_name, email, phone, password=None):
        if not user_name or len(user_name) <= 0:
            raise ValueError("Users must have a valid username")

        if not phone or len(phone) <= 0:
            raise ValueError('Phone number is required')

        if not email or len(email) <= 0:
            raise ValueError("Email field is required")

        if not password or len(password) < 8:
            raise ValueError("Password should be at least 8 characters long")

        email = email.lower()
        user = self.model(
            user_name=user_name,
            email=email,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Method to filter queryset by user type
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=models.User.Types.SUPORTER)