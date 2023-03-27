# Adventure-Quest...
Amusement Park Booking Website with Django and Python

### Setting up project

- Fork the repository
- Clone repository (If forked, can use the forked repo link)
```commandline
$ git clone https://github.com/Anureet19/AdventureQuestWeb.git
$ cd AdventureQuestWeb
```
- Module installation
```commandline
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
- Database setup
```commandline
$ python manage.py makemigrations
$ python manage.py migrate
```
- Create superuser
```commandline
$ python manage.py createsuperuser
```
- Start the application
```commandline
$ python manage.py runserver
```

### TO-DO
- [x] Signup with user verification
- [x] User authentication and login with email and password
- [x] Information page (Park timings & other relevant information)
- [x] A page for upcoming offers and discounts
- [x] Live location feature to show/direct to the park's location
- [x] Allowing booking for multiple tiers passes which could include daily, monthly or yearly passes for full or partial access to different rides and adventure activities.
