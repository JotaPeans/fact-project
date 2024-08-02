from .decodeJwt import decode_jwt

def get_jwt_token(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)
    if auth_header:
        # O token geralmente vem no formato "Bearer <token>"
        parts = auth_header.split()
        if len(parts) == 2 and parts[0].lower() == 'bearer':
            payload = decode_jwt(parts[1])
            return payload
    return None
