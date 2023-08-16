# endpoints

## adds  (16-8)

* [x] get adds list
* [x] get adds details
* [x] get categories list

## address (17-8)

* [x] get user addresses list
* [x] update user address
* [x] create user address

## notifications (17-8)

* [ ] get notifications list

## orders (17-8)

* [x] get orders list filtered by user
* [x] get orders details

## restaurants (21-8)

* [x] get restaurants list
    > filters : meal_category is_open_buffet
    > search : name_en - name_ar
    > order : rate
    > annotate start_with (lowest meal price in the restaurant) - OpenBuffetPackage count (min_count , max_count)
* [x] get restaurants details

## meals  (21-8)

* [ ] get meals list
    > filters : restaurant
    > pagination : None
    > annotate category name

## meal options  (21-8)

* [ ] get meal_options list
    > filters : meal - is_additional

## Open Buffet  (21-8)

* [ ] get Package list
    > filters : restaurant
    > pagination : None
    > annotate category name
* [ ] get Open Buffet Package Options list
    > filters : package - is_additional

## hotel   (21-8)

* [ ] get Hotel list
  > annotate: Hall (min - max)
* [ ] get Hotel details
* [ ] get halls list
    > filters: hotel
    > pagination : None
    > annotate category name  - hall images
* [ ] get halls options list
    > filters: hall

## user

* [X] register - login  by number
* [X] update user
* [ ] get promo codes list filtered by user and generic codes

cart is missing
socket is missing