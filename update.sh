date +"%m_%d_%Y_%T" > version
git add .
git commit -am "Update version for cron"
git push heroku master
