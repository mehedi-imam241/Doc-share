import  jwt
import datetime
import os

JWT_SECRET_KEY = os.getenv('JWT_SECRET')

def getJWT(user):
    payload = {
        'id': user.id,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10)
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

def verifyJWT(token):
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        return None