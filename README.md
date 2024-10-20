# PET RESCUE AND MANAGEMENT
 
This is a web application built using Python and the Django framework. The platform is designed to help shelters and rescue organizations manage rescued pets, handle adoption requests, and track pet care services such as boarding and grooming. Additionally, pet owners can add and manage their own pet's details.

Features
Pet Rescue and Adoption Management: Shelters can manage rescued pets and handle adoption processes.
Pet Boarding and Grooming: Offers services for boarding and grooming pets.
User Pet Management: Users can add and manage details of their personal pets.
Installation and Setup
Prerequisites:
Python (version 3.6 or higher)
XAMPP (Apache server and MySQL database)
Django (to be installed in a virtual environment)
Step 1: Setting Up the Environment
Download and install XAMPP for Apache and MySQL.
Open XAMPP Control Panel, start the Apache and MySQL modules.
Step 2: Project Setup
Clone the repository to your local machine.




bash
Copy code
cd pet-rescue-management
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

For Windows:
bash
Copy code
.\env\Scripts\activate
For macOS/Linux:
bash
Copy code
source env/bin/activate
Step 3: Install Required Packages
Install Django using pip:

bash
Copy code
pip install django
Step 4: Database Configuration
Open phpMyAdmin from XAMPP to create a new MySQL database.

Update the settings.py file in your Django project with the database configuration:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Step 5: Running Migrations
Make and apply migrations to create database tables:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Step 6: Running the Server
To start the development server, run:

bash
Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to view the platform.

Usage
Shelters and rescue organizations can manage pets and handle adoption requests.
Users can book boarding and grooming services for their pets.
Pet owners can add and manage their own pets' details.
