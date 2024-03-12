# crypto_station_front_end

![Crypto Station Architecture](https://github.com/thomasbs17/crypto_station_front_end/assets/64446011/2b3795fa-89cf-4f30-a3fb-98a9bc082762)

To kill/stop containers (in powershell):
- docker stop (docker ps -q)
- docker rm (docker ps -aq)


To build Docker:
docker build -f front_end/Dockerfile -t my-frontend .

To run Docker:
docker run -p 3000:3000 my-frontend

To compose down (docker-compose):
docker-compose down -v

To compose up and build:
docker-compose up --build

To compose up (run all containers):
docker-compose up
