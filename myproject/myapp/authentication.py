from rest_framework import authentication

class BearerAuthentication(authentication.TokenAuthentication):
    '''
    Authentication class to facilitate API connection through Postman
    '''
    keyword = 'Bearer'