from pyjserver import Endpoint

e = Endpoint('nossa-api', db_file_path='./db.json')
e.run()

