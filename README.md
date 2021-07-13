Abstract
--------
This is a simple todo list application.
It is made using Django/DRF framework and represents simple application, where users can make an items in todo list with title and description.
For data storage the PostgreSQL database may be utilized.

Requirements
------------
1. Install all the required modules:
  `pip install -r requirements.txt`
3. Create new database `todo` in PostgreSQL.
2. Run the migration:
  `python manage.py migrate`
3. Make sure to create `.env` file in your project root directory according to the `.env.example`.

Instructions
------------
1. Run server:
  `python manage.py runserver`
2. To create a user: go to <http://127.0.0.1:8000/user/signup/>. Note: only authenticated users can create/retrieve/update/delete todo items.
3. To login the user: go to <http://127.0.0.1:8000/user/login/>.
4. To create a todo item: go to <http://127.0.0.1:8000/todo/>.
5. To retrieve/update or delete the created todo item: go to <http://127.0.0.1:8000/todo/1/>.
