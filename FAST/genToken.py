import jwt

def createToken(datos:dict):
    token:str=jwt.encode(payload=datos,key='secretkey',algorithm='HS265')
    return token