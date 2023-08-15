# endpoints

## adds

* [ ] get adds list
* [ ] get adds details
* [ ] get categories list

## address

* [ ] get user addresses list
* [ ] update user address
* [ ] create user address

## notifications

* [ ] get notifications list

## restaurants

* [ ] get restaurants list
    > filters : meal_category is_open_buffet
    > search : name_en - name_ar
    > order : rate
    > annotate start_with (lowest meal price in the restaurant) - OpenBuffetPackage count (min_count , max_count)
* [ ] get restaurants details

## meals

* [ ] get meals list
    > filters : restaurant
    > pagination : None
    > annotate category name

## meal options

* [ ] get meal_options list
    > filters : meal - is_additional

## Open Buffet

* [ ] get Package list
    > filters : restaurant
    > pagination : None
    > annotate category name
* [ ] get Open Buffet Package Options list
    > filters : package - is_additional

## hotel

* [ ] get Hotel list
  > annotate: Hall (min - max)
* [ ] get Hotel details
* [ ] get halls list
    > filters: hotel
    > pagination : None
    > annotate category name  - hall images
* [ ] get halls options list
    > filters: hall

## orders

* [ ] get orders list filtered by user
* [ ] get orders details

## user

* [ ] register - login  by number
* [ ] update user
* [ ] get promo codes list filtered by user and generic codes


cart is missing