# Medical Diagnosis App

The Medical diagnosis app is a challenge created by the mpharma dev team to stub out a RESTful API to allow for the utilization of an internationally recognized set of diagnosis codes. 
Functional Requirements are;
  - Create a new diagnosis code record
  - Edit an existing diagnosis code record
  - List diagnosis codes in batches of 20 (and paginate through the rest of the record)
  - Retrieve diagnosis codes by ID
  - Delete a diagnosis code by ID

Non-functional Requirements
  - All API endpoints should respond within 100ms
  - Add Unit tests to the code
  - Add a readme to the project

# Setting Up the application
Clone the application to your local machine.
Navigate to the application folder in the terminal and run the following commands
```sh
$ docker-compose build
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py seed
$ docker-compose run web python manage.py test
$ docker-compose up
```
This will create a docker image of the application, download the necessary dependencies, migrate the database, also setup the demo data(which is the ICD-10 list), run all tests and start the server.

Verify the deployment by navigating to your server address in postman or your preferred API Client app.

```sh
POST
Create a new record
http://127.0.0.1:8000/api/v1/diagnosis_codes/
Sample Json
{
    "category_code": "A007",
    "diagnosis_code": "089",
    "full_code": "A0007089",
    "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
    "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
    "category_title": "Cholera"
}

GET
Retrieve all records
http://127.0.0.1:8000/api/v1/diagnosis_codes/

GET, PUT and DELETE
Retrieve, update and delete a single record
http://127.0.0.1:8000/api/v1/diagnosis_codes/<pk>
```

License
----

MIT