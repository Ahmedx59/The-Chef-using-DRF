- add media and static settings (X)
- add .gitignore file (search on google) (X)

task 1
- add field user to resturant (X)
- add tag field in resturant as choices (find choices on gpt ) (X)
- change avilable field in table to boolean field (X)
- resturant endpoint(list- detail - update):(X)
	- update: only the user that owns the resturant can update it (X)
	- prevent other user from using update endpoint (X)
	
- add filter by (tag - ) (X)
- add search (name - min price) (X)

task 2
- table endpoint(list - create - update - delete):(X)
	- list: only view taples of same resturant , and is avilable (X)
	- create, update, delete: only user of the resturant can do tables (X)
		- prevent other user from using create, update, delete endpoint

task 3
- add signal that create a resturant after user(seller صاحب مطعم) is created (X)


task 4 
- add meals models(X)
- add endpoint for meals(list - detail - update - create - delete):(X)
		- list: view only meals of the same resturant (X)
		- update, create, delete: only the resturant owner can do them

coupon
seller dashboard
payment




app order :



cart:
    user
    total
    coupon
    total_after_coupon
    is_completed

meals detail:
    cart
    meal
    quantity
    price
    total

order:
    cart
    code
    status
    created_at
    delivery_time
    delivery_location
    