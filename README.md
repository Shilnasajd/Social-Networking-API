# Social-Networking

## Setup

1. Clone the repository
```
git clone https://github.com/Shilnasajd/Social-Networking-API.git
```

2. Install Virtual Environment
   - cd Social-Networking-API/
#### Ubuntu
```
sudo apt update
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
```
#### Windows
```
python -m venv env
env\Scripts\activate
```
. Install Requirements
```
pip install -r requirements.txt
```
## Run

1. Enter into the project directory

   - Make sure you're in the root directory of your Django 
project where manage.py is located.

#### Ubuntu
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
#### Windows
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
2. Access the Swagger UI of the API
   - Open your web browser and navigate to:
```
localhost:8000/swagger/
```
## Check API's

1. Postman collection Link
```
https://drive.google.com/file/d/1z3Bsqx6P2MY_vqIDN6LT5FyCXjd8SDrt/view?usp=sharing
```
## Docker

### Ubuntu

1. Update package list:
```
sudo apt update
```
2. Install prerequisites:
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
3. Add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
4. Add Docker’s APT repository:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
5. Update package list again:
```
sudo apt update
```
6. Install Docker CE (Community Edition):
```
sudo apt install docker-ce
```
7. Start the Docker service:
```
sudo systemctl start docker
```
8. Enable Docker to start on boot:
```
sudo systemctl enable docker
```
9. Check Docker version:
```
docker --version
```
10. Add current user to the Docker group:
```
sudo usermod -aG docker $USER
```

11. Build Docker images defined in the Docker Compose file:
```
docker-compose build
```
12. Start services defined in the Docker Compose file:
```
docker-compose up
```
13. Start services in the background (detached mode):
```
docker-compose up -d
```

