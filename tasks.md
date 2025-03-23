- add media and static settings (X)
- add .gitignore file (search on google) (X)

task 1
- add field user to restaurant (X)
- add tag field in restaurant as choices (find choices on gpt ) (X)
- change available field in table to boolean field (X)
- restaurant endpoint(list- detail - update):(X)
	- update: only the user that owns the restaurant can update it (X)
	- prevent other user from using update endpoint (X)
	
- add filter by (tag - ) (X)
- add search (name - min price) (X)

task 2
- table endpoint(list - create - update - delete):(X)
	- list: only view tables of same restaurant , and is available (X)
	- create, update, delete: only user of the restaurant can do tables (X)
		- prevent other user from using create, update, delete endpoint

task 3
- add signal that create a restaurant after user(seller) is created (X)


task 4 
- add meals models(X)
- add endpoint for meals(list - detail - update - create - delete):(X)
		- list: view only meals of the same restaurant (X)
		- update, create, delete: only the restaurant owner can do them

coupon(X)




seller dashboard (
    total booking (active - ended - canceled)(X)
    total orders
    total meals(n,d,f)(X)
    total tables
    total chef
)


TODO:
    payment
    review
