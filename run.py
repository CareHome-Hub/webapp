#!/usr/bin/python
from web import app
import connexion

# app = connexion.App(__name__, specification_dir='web/swagger/')
# app.add_api('my_api.yaml')
app.run(debug=True, host='0.0.0.0', port=8999)
