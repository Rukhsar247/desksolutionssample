from django.contrib.auth.models import BaseUserManager


class OrganizationHeadManager(BaseUserManager):
    def create_user(self, email, title, password=None):
        if not email:
            raise ValueError("Email is reuqired")
        if not title:
            raise ValueError("Title is required")

        user = self.model(
            email=self.normalize_email(email),
            title=title
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, title, password):
        user = self.create_user(
            email=self.normalize_email(email),
            title=title,
            password=password,
        )

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
