import bcrypt

class Encriptar:
    def encriptar_password(password):
        salt = bcrypt.gensalt()
        print('salt', salt)
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    def verificar_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))