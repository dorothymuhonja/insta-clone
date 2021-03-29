# insta-clone

### By Dorothy Muhonja

## Description
This is a instagram-like app where a user can share like and comment on images.

### Set Up Instruction
* Python 3.6 and above
* Editor
* Virtual environment (optional)
*  Django
* SQLAlchemy (Postgres)

## Technologies used
* Python3
* Django
* css3
* html5
* Bootstrap


## Installation and setup
 Clone this repo
 ```
 git clone https://github.com/dorothymuhonja/insta-clone.git
 ```

 ### Create and activate a virtual environment
 
    virtualenv venv --python=python3

    source venv/bin/activate

### Install django
    pip install django (and other dependencies required)

### Copy environment variable
    cp env.sample .env

### Load/refresh .environment variables
    source .env

### Running the app
```
python3 manage.py runserver
```
## Behaviour Driven Development (BDD)
#### User
* Register an account and log in.
* Upload pictures to your account
* Search for other users' profiles
* Set up your own profile
* Like and comment on pictures
* Follow your favorite users

#### Admin
Can add, change or delete the pictures and comments

### Screenshots
 ![Landing Page](static/images/home.png)
![Gallery](static/images/gallery.png)
![Image details](static/images/details.png)

## Email Address
dorothymuhonja7@gmail.com

## License and Copyright

Copyright (c) 2021 Dorothy Muhonja

[MIT License](LICENSE)