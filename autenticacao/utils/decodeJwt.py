import jwt
from django.conf import settings

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as e:
        return None
    except jwt.InvalidTokenError:
        return None
