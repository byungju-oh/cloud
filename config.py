db = {
	'user' : 'ubuntu',
    'password' : 'ubuntu',
    'host' : '34.69.95.212',
    'port' : 3306,
    'database' : 'data'
}
DB_URL = f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"