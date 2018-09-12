from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def get_password(password):
    hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
    return hash_


def check_password(bcrypt_password, password):
    return bcrypt.check_password_hash(bcrypt_password, password)


if __name__ == "__main__":
    password = get_password('Red198594#')
    print(password)

