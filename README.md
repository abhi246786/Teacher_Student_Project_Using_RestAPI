

# REST-API-in-Django-using-Django-REST-Framework.
REST API in Django using Django REST Framework.

1. User Sign Up/Forgot Password APIs. 
2. Uses JWT authentication. 
3. Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Useinternal Django Groups to achieve the same). 
4. Teacher must be able to add/list the students. 
5. Admin must be able to add/list every user in the database.
6. Students must be able to see his information only. 


## urls

Django REST API Root:
http://127.0.0.1:8000/api/

Teachers Root:
http://127.0.0.1:8000/teachers/

Admin Root:
http://127.0.0.1:8000/admin/

Student Root:
http://127.0.0.1:8000/


# Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/abhi246786/Teacher_Student_Project_Using_RestAPI
```



Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

