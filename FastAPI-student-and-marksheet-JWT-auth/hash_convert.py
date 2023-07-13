from passlib.context import CryptContext
from routs.tokenAuth import verify_password
pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    def varify(plain_password,hashed_password):
        print(plain_password,hashed_password)
        return pwd_cxt.verify(plain_password, hashed_password)