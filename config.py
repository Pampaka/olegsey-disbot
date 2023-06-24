import os

settings = {
    'token': os.environ.get('TOKEN'),
    'bot': 'Olegsey',
    'id': os.environ.get('APP_ID'),
    'prefix': os.environ.get('PREFIX', '/')
}
