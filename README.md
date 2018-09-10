Item catalog

This project contains a catalog of teams and some players from those teams. You can edit, delete, create new players on the fly.

Preqrequisites

- vagrant
- python
- virtual box

Steps you need to follow to start

1) Install Vagrant and VirtualBox
2) Clone the fullstack-nanodegree-vm - github repo
3) Write your Flask application locally in the vagrant directory (which will automatically be synced to /vagrant within the VM).
4) Run your application within the VM (python /vagrant/catalog/project.py)
5) Access and test your application by visiting http://localhost:5000 locally 


Solution to some important issues that i faced.

1) Use this api which returns the email, name and picture from your google account
		https://www.googleapis.com/userinfo/v2/me
2) The scopes that you need to grant are
	https://www.googleapis.com/auth/userinfo.profile 
	https://www.googleapis.com/auth/userinfo.email
3) make sure to have this flag - check_same_thread, marked to false while calling create_engine
   engine = create_engine('sqlite:///restaurantmenu.db',
                       connect_args={'check_same_thread': False})

Credits - https://github.com/udacity/Full-Stack-Foundations
