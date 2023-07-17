<!-- 
Category 
    name

User
    type (consumer - delivery - restaurant - hotel)
    phone number
    otp

DeliveryCar
    user
    model
    plat

User Address
    User
    phone_number
    location
    street
    building
    floor
    apartment
    

Restaurant
    name
    phone
    logo
    description
    rate
    is_open_buffet
    admin_user
    #category

Branch
    restaurant
    admin_user
    phone
    location
    street
    building
    is_available
    max_orders : int

Meal
    restaurant
    #category
    name
    image
    description
    price
    is_available

RestaurantOpenBuffet
    restaurant
    clients_count
    price

Hotel
    name
    description
    address
    max_persons

HotelPlans
    hotel
    number_of_guests
    price
    services

Hotel_images
    hotel
    image

Ads
    name
    photo
    description
    link

Terms and Conditions
    text

About
    text
    instagram
    twitter
    facebook
    snapchat
    whatsapp

Contact Us
    text

UserFavorites
    user
    meal

Order
    user
    type ()
    user_address
    delivery_user
    status (canceled - returned - delivering - preparing - delivered)
    payment_type
    is_checkout
    is_paid
    payment_url
    note
    ordered_time
    scheduled_time
    estimated_time
    delivered_time

OrderMeal
    order
    meal
    quantity
    note
 -->

not_ready_yet
    hotel
    open buffet