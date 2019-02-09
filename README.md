# hsc-be


## Installation
1. Prerequisite

 - Docker
 - Docker compose

2. Installation.
 - Install requirements using:
```bash
   docker-compose build
```
 
 - Run server:
``` bash
   docker-compose up    
````
 - (Optional): Create superuser account with **username/password**: **admin/testing123** by using:
 
 ``` bash
    ./docker-django.sh loaddata users
 ```

 3. API Documentation
    (Provided)
