# run.py

##Change this back once ready to deploy to heroku. Running locally for development purposes

import os
from project import app
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

#from project import app
#app.run()