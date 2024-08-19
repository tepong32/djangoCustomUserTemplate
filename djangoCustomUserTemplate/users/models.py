from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Please provide a valid Email Address.")
		email = self.normalize_email(email) ### cleaning the data
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.set_default('is_staff', False)
		extra_fields.set_default('is_admin', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.set_default('is_staff', True)
		extra_fields.set_default('is_admin', True)
		return self._create_user(email, password, **extra_fields)


class NormalizedCharField(models.CharField):
	"""Custom CharField to make sure that fields that will use the CharField will have its data cleaned."""
	
	def to_python(self, value):
		return value.strip().title()


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(blank=True, default="", unique=True)
	name = NormalizedCharField(max_length=255, blank=True, default=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(blank=True, null=True) ### args here are my previous error for there's no last_login for newly-created users
	objects = CustomUserManager() ### this is what makes the call User.objects.xxx call use the CustomUserManager instead of the default
	USERNAME_FIELD = 'email' ### login using email
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []
	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	def get_full_name(self):
		return self.name
	def get_short_name(self):
		return self.name




