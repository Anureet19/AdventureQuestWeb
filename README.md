# Adventure-Quest...
Amusement Park Booking Website with Django and Python

### Setting up project

- Fork the repository
- Clone repository (If forked, can use the forked repo link)
```commandline
$ git clone https://github.com/simranarora5/AdventureQuest.git
$ cd AdventureQuest
```
- Module installation
```commandline
$ virtualenv env
$ source env/bin/activate
$ pip install django
```
- Database setup
```commandline
$ python manage.py makemigrations
$ python manage.py migrate
```
- Start the application
```commandline
$ python manage.py runserver
```

### TO-DO
- [ ] Signup with user verification
- [ ] User authentication and login with email and password
- [ ] Information page (Park timings & other relevant information)
- [ ] A page for upcoming offers and discounts
- [ ] Live location feature to show/direct to the park's location
- [ ] Price filtering (Variable pricing for adults & children)
- [ ] Allowing booking for multiple tiers passes which could include daily, monthly or yearly passes for full or partial access to different rides and adventure activities.
