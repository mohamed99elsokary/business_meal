# endpoints

## adds  (16-8)

* [X] get adds list
* [X] get adds details
* [X] get categories list

## address (17-8)

* [X] get user addresses list
* [X] update user address
* [X] create user address

## notifications (17-8)

* [ ] get notifications list

## orders (17-8)

* [X] get orders list filtered by user
* [X] get orders details

## restaurants (21-8)

* [X] get restaurants list
  > filters : meal_category is_open_buffet
  > search : name_en - name_ar
  > order : rate
  > annotate start_with (lowest meal price in the restaurant) - OpenBuffetPackage count (min_count , max_count)
  >
* [X] get restaurants details

## meals  (21-8)

* [X] get meals list
  > filters : restaurant
  > pagination : None
  > annotate category name
  >

## meal options  (21-8)

* [X] get meal_options list
  > filters : meal - is_additional
  >

## Open Buffet  (21-8)

* [X] get Package list
  > filters : restaurant
  > pagination : None
  > annotate category name
  >
* [X] get Open Buffet Package Options list
  > filters : package - is_additional
  >

## hotel   (21-8)

* [X] get Hotel list
  > annotate: Hall (min - max)
  >
* [X] get Hotel details
* [X] get halls list
  > filters: hotel
  > pagination : None
  > annotate category name  - hall images
  >
* [X] get halls options list
  > filters: hall
  >

## user

* [X] register - login  by number
* [X] update user
* [ ] get promo codes list filtered by user and generic codes

cart is missing
socket is missing
