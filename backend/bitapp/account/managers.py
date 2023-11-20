from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager
from .models import User


class UserManager(BaseUserManager):
    def create_user(self, email, phone, f_name, l_name, password=None):
        if not phone:
            raise ValueError("Users must have an phone")

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            f_name=f_name,
            l_name=l_name,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, f_name, l_name, password=None):
        user = self.create_user(
            phone=phone,
            email=self.normalize_email(email),
            f_name=f_name,
            l_name=l_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class  SimpleUserManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SIMPLE_USER)
    

class SingerManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SINGER)
    

class ProducerManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PRODUCER)
    

class SupporterManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SUPPORTER)