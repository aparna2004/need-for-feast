from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator,MaxValueValidator


# # Create your models here.
# class User(AbstractUser):
#     pass


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "Owner"
        CUSTOMER = "CUSTOMER", "Customer"
        DELIVERER = "DELIVERER", "Deliverer"

    base_role = Role.ADMIN
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"    
    name = models.CharField(max_length=100,null=True)
    is_staff = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ADMIN)
   # customer = models.ManyToManyField(to = 'self', related_name='deliverer',symmetrical=False)
    REQUIRED_FIELDS = ['username']
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class OwnerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.OWNER)


class Owner(User):
    base_role = User.Role.OWNER
    owner = OwnerManager()
    class Meta:
        proxy = True

# customer
class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):
    base_role = User.Role.CUSTOMER

    customer =CustomerManager()

    class Meta:
        proxy = True


class PhoneNumbers(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    phone_number = models.CharField(max_length=10)

class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=20)

class CustomerProfile(models.Model):
    class Preferences(models.TextChoices):
        VEG = 'VEG','veg'
        NONVEG = 'NONVEG', 'nonveg' 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preference = models.CharField(null=True, max_length = 30, choices=Preferences.choices, default=Preferences.VEG)


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)



#deliverer

class DelivererManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DELIVERER)


class Deliverer(User):
    base_role = User.Role.DELIVERER

    deliverer = DelivererManager()

    class Meta:
        proxy = True


class DelivererProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=20)

@receiver(post_save, sender=Deliverer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DELIVERER":
        DelivererProfile.objects.create(user=instance)
                                      
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)

class Items(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200, null=True)
    veg = models.CharField(max_length=7, default="Veg")
    image = models.ImageField(upload_to="images/")
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Items, related_name="placed", blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.created_on}+ {self.price}"
    
class CustomerDelivererRelationship(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='deliverer')
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE, related_name='customer')
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])


@receiver(post_save, sender=CustomerDelivererRelationship)
@receiver(post_delete, sender=CustomerDelivererRelationship)
def update_deliverer_rating(sender, instance, **kwargs):
    deliverer = instance.deliverer
    deliverer_ratings = CustomerDelivererRelationship.objects.filter(deliverer=deliverer)
    total_ratings = deliverer_ratings.count()
    if total_ratings > 0:
        total_rating = sum(rating.rating for rating in deliverer_ratings)
        deliverer.rating = total_rating / total_ratings
    else:
        deliverer.rating = 0.0
    deliverer.save()
