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
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, password, **extra_fields)


###### not working as intended so removed
# class NormalizedCharField(models.CharField):
# 	"""Custom CharField to make sure that fields that will use the CharField will have its data cleaned."""
	
# 	def to_python(self, value):
# 		if isinstance(value, bool):
# 			# Convert boolean to string representation
# 			value = str(value)
# 			return value.strip().title()


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(blank=True, default="", unique=True)
	name = models.CharField(max_length=255, blank=True, default=True)
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
		return self.name or self.email.split('@')[0]







class Profile(models.Model):

	# profile-related stuffs 
	user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted, the profile will be deleted, too
	alias = models.CharField(blank=True, null=True, max_length=50, unique=True, verbose_name="Alias: ",help_text="(-_-)") 
	# Male = "Male"
	# Female = "Female"
	# Neutral = "Neutral"
	# gender_choice = [
	# 	(Male, "Male"),
	# 	(Female, "Female"),
	# 	(Neutral, "Neutral")
	# ]
	# gender = models.CharField(
	# 	max_length=10,
	# 	choices=gender_choice,
	# 	default=Neutral, verbose_name="Gender: "
	# )
	location = models.CharField(blank=True, null=True, max_length=255, default="Uh...Earth?", verbose_name="Location: ", help_text="Do you want to fill this out? :D")

	# Other information that can be displayed on a user profile page:
	quote = models.CharField(blank=True, max_length=300, verbose_name="Quote you live by: ", help_text="'Pampa-Angas'")
	about_me = models.TextField(blank=True, default="...Default About Me text", help_text="Tell us something about you.")
	
	def dp_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP/<username>/<filename> ---check settings.py. MEDIA_ROOT=media for the exact folder/location
		return 'users/{}/DP/{}'.format(instance.user.username, filename)
	image = models.ImageField(default='defaults/round.png', blank=True, upload_to=dp_directory_path, verbose_name="Profile Picture: ", help_text='Help us recognize you. ;)')


	def __str__(self):
		return f"{self.user.username}"

	def get_absolute_url(self):
		return reverse('profile', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):		# for resizing/downsizing images
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)	# open the image of the current instance
		if img.height > 600 or img.width > 600:	# for sizing-down the images to conserve memory in the server
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)