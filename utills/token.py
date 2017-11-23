def req_to_token(request):
    import jwt
    from lottery_admin.settings import SECRET_KEY

    auth = request.META.get('HTTP_AUTHORIZATION', 'unkown')
    token = auth[4:].strip()
    token_data = jwt.decode(token, SECRET_KEY)
    return token_data