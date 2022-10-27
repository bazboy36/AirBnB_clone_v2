#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static

#install NginX
sudo apt-get -y update
sudo apt-get -y install nginx

#configure nginx firewall
sudo ufw allow 'Nginx HTTP'

#create folders if they dont exist
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

#create fake HTML file
echo "<h1>Welcome to www.daviesajayi.tech</h1>" > /data/web_static/releases/test/index.html

#Create a symbolic link /data/web_static/current for /data/web_static/releases/test/ folder. 
#if the symbolic link already exists, 
#it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give recursive ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '39i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#create a symbolic link /etc/nginx/sites-enabled/default for /etc/nginx/sites-available/default
#if the symbolic link already exists,
#it should be deleted and recreated every time the script is ran.
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

#restart nginx
sudo service nginx restart
