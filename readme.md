# Useful Commands
sudo docker build -t flask-app:0.1.0 .
sudo docker run -d -p 7000:80 --name="FlaskApp" flask-app:0.1.0