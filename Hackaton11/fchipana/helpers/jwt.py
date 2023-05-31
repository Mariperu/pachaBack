import jwt

secret_key  = "nasdjndlfainli#@#@#@#@#@#"

class generarToken:
    def generar_token(payload):
        try:
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            return token
        except:
            print('No se pudo generar el Token')