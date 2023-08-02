pip install --upgrade pip

pip install discord.py[voice]
pip install python-dotenv

# GIT

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:alexsagarra/dachbot.git
git push -u origin main

# Server

server settings
https://cloud.digitalocean.com/droplets/
164.90.238.9

## SSH

```
ssh-keygen
```

--> copy to githup

## PM2

https://pm2.io/docs/runtime/guide/installation/

```
apt install npm
npm install pm2 -g
pm2 completion install
npm install pm2 -g && pm2 update
```

pm2 start script.py --name appname --interpreter python3
