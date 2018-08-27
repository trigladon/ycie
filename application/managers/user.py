from django.contrib.auth.models import UserManager as DjUserManager


__all__ = (
    'UserManager',
)


class UserManager(DjUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # username = self.model.normalize_username(username)
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        return super(UserManager, self).create_superuser(username=None, email=email, password=password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        return super(UserManager, self).create_user(username=None, email=email, password=password, **extra_fields)