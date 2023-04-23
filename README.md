# Microservices-Based-Architecture


Converted a monolith architecture based docker-compose application into a microservices based architecture.


To run just execute:
docker compose up


This is run all microservices running in different ports virtulized to the landing page's port(5050)


Apart from the four basic arithmetic services (addition, substraction , multiplication and division) , the three other services that are added are equals,exponent and modulus



The directory structure of every microservice:

├── <name of the service>
  
│   ├── Dockerfile          
  
│   ├── app
  
│   │   ├── app.py          \
  
│   │   └── requirements.txt # same as landing/app/requirements.txt
  
│   │  
  
  
  
The landing page has been beautified :
  
  ![image](https://user-images.githubusercontent.com/105477488/233857893-5e0b8426-9cbf-4bb3-8781-599d70688810.png)


