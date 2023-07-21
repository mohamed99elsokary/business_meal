from django.db import models

from business_meal.userapp.models import Address, User


class Restaurant(models.Model):
    # relations
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/")
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


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    delivery_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="delivery_user"
    )
    user_address = models.ForeignKey(Address, on_delete=models.CASCADE)
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


class OrderMeal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    note = models.CharField(max_length=50)


class OrderMealOption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    option = models.ForeignKey(MealOptions, on_delete=models.CASCADE)


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

    def __str__(self):
        return self.code


class RestaurantOpenBuffet(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # fields
    clients_count = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.name}"


# class Hotel(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     max_persons = models.IntegerField()

#     def __str__(self):
#         return self.name


# class HotelPlans(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     number_of_guests = models.IntegerField()
#     price = models.IntegerField()
#     services = models.CharField(max_length=50)

#     def __str__(self):
#         return self.hotel.name


# class HotelImages(models.Model):
#     # relations
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     # fields
#     image = models.ImageField(upload_to="media/")

#     def __str__(self):
#         return self.name
