Abstract
--------
This is a simple todo list application.
It is made using Django/DRF framework and represents simple application, where users can make an items in todo list with title and description.
For data storage the PostgreSQL database is utilized.

Requirements
------------
1. Install all the required modules:
  `pip install -r requirements.txt`
3. Create new database `todo` in PostgreSQL.
2. Run the migration:
  `python manage.py migrate`
3. The project uses default insecure SECRET_KEY. Make sure to create `.env` file according to the `.env.example` (don't forget to include the following parameters: SECRET_KEY, DATABASE_USER, DATABASE_PASS). Also refer to [this link](https://www.youtube.com/watch?v=5iWhQWVXosU&t=0s) for detailed information (note: for Ubuntu use `.bashrc` instead of `.bash_profile`).

Instructions
------------
1. Run server:
  `python manage.py runserver`
2. To create a user: go to <http://127.0.0.1:8000/user/signup/>. Note: only authenticated users can create/retrieve/update/delete todo items.
3. To login the user: go to <http://127.0.0.1:8000/user/login/>.
4. To create a todo item: go to <http://127.0.0.1:8000/todo/>.
5. To retrieve/update or delete the created todo item: go to <http://127.0.0.1:8000/todo/1/>.








Abstract
--------
This is a test task for Apollo co. to assess my skills for the Junior Python (Django/DRF) position.
The task itself was to create a simple event management system, where current user could create (POST) events in the following format:
    
    {
    "event_type": <event_type_name>
    "info": <anybody json>
    "timestamp": <datetime>
    }
    
To achieve this, application has to have two models:
    
    Event(
        id, 
        user: fk field, 
        event_type: fk field, 
        info: JSON field, 
        timestamp: datetime field, 
        created_at: auto_now datetime field
    ) 
    
    EventType(
        id, 
        name: char field
    )

Preparation
----------
1. Make sure to install all the required modules (see file 'requirements.txt'):
`pip install -r requirements.txt`
2. Install Postman (follow the URL provided):
https://www.tecmint.com/install-postman-on-linux-desktop/
3. Create a new database using PostgreSQL.
4. Create a new .env file in the directory, where settings.py file is located; open the file and fill in the following:
    
    `SECRET_KEY=t3tqew(dj%b0#nzqk8=dc-&e5&&s=42@hzr7o@n-lq(-q)b!ql`  
    `DATABASE_NAME=testtask`  
    `DATABASE_USER=postgres`  
    `DATABASE_PASS=qwerty`  
    
Note: values are shown for reference only and may differ, depending on your db settings.  
5. Perform migration:
    `python manage.py migrate`

Instructions
------------
1. Create superuser:
    `python manage.py createsuperuser`
2. Run the server:
    `python manage.py runserver`
3. Open the Postman, go to http://127.0.0.1:8000/user/login, choose method POST and in request body fill in 'username' and 'password', created at the step 1.
4. Obtain and copy the token in the response body.
5. Go to http://127.0.0.1:8000/event/type, choose method POST and in request body fill in event type 'name', in request headers key put 'Authorization', value 'Token <Ctrl+V to past copied token>'
6. Go to http://127.0.0.1:8000/event/, choose method POST and in request body fill the following keys / values:  
    `KEY: event_type   |     VALUE: 1`   
    `KEY: info         |     VALUE: {"key1": "value1", "key2": "value2"}`   
7. Use method GET to watch the result.
8. Go to http://127.0.0.1:8000/user/logout, choose method GET to logout the current user.


