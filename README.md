# library-catalog-site
Library catalog application using Django for library users and librarians

## Setup

1. After cloning the repository, setup your virtual environment with `virtualenv <enviornment-name>` and install dependencies using the requirements.txt file provided
2. Add a .env file to the main directory and add the following 
    `SECRET_KEY=<your secret key>`
3. Run the following commands inside of the virtual envionment
    `python manage.py migrate`
    `python manage.py runserver`

