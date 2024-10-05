from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,UserName,Email,password, *extra_fields):
        if not UserName:
            raise ValueError ("UserName Need Unique")
        if not Email:
            raise ValueError("Email must be Unique")
        email =self.normalize_email(Email)
        user=self.model(
            UserName=UserName,
            Email=Email,
            *extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self,UserName,Email,password,*extra_fields):
        user=self.create_user(
            UserName=UserName,
            Email=Email,
            password=password,
            *extra_fields
        )
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save(using=self._db)
        return user