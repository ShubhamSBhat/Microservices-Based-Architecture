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
  
  ![image](https://user-images.githubusercontent.com/105477488/233857752-de324561-6c58-4692-a160-d6149c5d4aa8.png)

