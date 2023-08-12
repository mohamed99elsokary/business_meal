from django.db import models

from business_meal.userapp.models import Address, User


class Category(models.Model):
    # relations
    image = models.ImageField(upload_to="media/", null=True, blank=True, default=None)
    name = models.CharField(max_length=50)
    # fields

    def __str__(self):
        return str(self.name)


class Restaurant(models.Model):
    # relations
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/")
    cover_photo = models.ImageField(
        upload_to="media/", null=True, blank=True, default=None
    )
    description = models.CharField(max_length=50)
    is_open_buffet = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    max_orders = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant} {self.street}"


class Meal(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/")
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MealOptions(models.Model):
    # relations
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    # fields
    option = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    is_additional = models.BooleanField(default=False)

    def __str__(self):
        return self.option


class OpenBuffetPackage(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    # fields
    name = models.CharField(max_length=50, default=None, null=True, blank=True)
    clients_count = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.name}"


class OpenBuffetPackageOptions(models.Model):
    # relations
    package = models.ForeignKey(OpenBuffetPackage, on_delete=models.CASCADE)

    # fields
    option = models.CharField(max_length=50)
    is_additional = models.BooleanField(default=False)
    price = models.IntegerField(default=None, null=True, blank=True)


class UserFavorites(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class PromoCode(models.Model):
    code = models.CharField(max_length=50)
    times_to_use = models.IntegerField()
    used_times = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.code


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/", null=True, blank=True, default=None)
    cover_photo = models.ImageField(
        upload_to="media/", null=True, blank=True, default=None
    )
    description = models.TextField()
    address = models.CharField(max_length=50)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.name


class Hall(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    min = models.IntegerField(help_text="number of guests", default=0)
    max = models.IntegerField(help_text="number of guests", default=0)
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.hotel.name


class HallOptions(models.Model):
    # relations
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    option = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.option


class HallImages(models.Model):
    # relations
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.nameuser_address


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    delivery_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="delivery_user"
    )
    user_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    promo = models.ForeignKey(
        PromoCode, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    type = models.CharField(max_length=50)
    status = models.CharField(
        max_length=50,
        choices=[
            ("preparing", "preparing"),
            ("delivering", "delivering"),
            ("delivered", "delivered"),
            ("canceled", "canceled"),
            ("is_paid", "is_paid"),
        ],
    )
    payment_type = models.CharField(max_length=50)
    is_checkout = models.BooleanField()
    is_paid = models.BooleanField(default=False)
    payment_url = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    ordered_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    scheduled_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    estimated_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    delivered_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    package = models.ForeignKey(
        OpenBuffetPackage,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField()
    note = models.CharField(max_length=50)


class OrderItemOption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal_option = models.ForeignKey(
        MealOptions,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    package_option = models.ForeignKey(
        OpenBuffetPackageOptions,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
