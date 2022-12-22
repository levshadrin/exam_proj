import os

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = 27017

MONGO_DBNAME = 'rest'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
}

people = {
    'item_title': 'person',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {
    'people': people,
}
