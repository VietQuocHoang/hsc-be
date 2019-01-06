# hsc-be


## Installation
1. Prerequisite.

    This section will be removed in the future.

 - Python3
 - PostgreSQL.
 - (Optional) Virtualenv. 
 - Pip.

2. Installation.
 - Install requirements using:
```bash
    python3 -m pip install -r requirements.txt
```
 - Migrate data:
``` bash
    python3 manage.py migrate
```
 
 - Run server:
``` bash
    python3 manage.py runserver
````
 - (Optional): Create superuser account with **username/password**: **admin/testing123** by using:
 
 ``` bash
    python3 manage.py loaddata users
 ```

 3. API Documentation
    (Provided)