# run this command to make the lib folder for running
# third party apps in Google App Engine. need to call the
# target folder lib since it is called lib in appengine_config;
# run command in directory with app.yaml

pip freeze -r requirements.txt -t lib
