from typing import Annotated
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import routs.tokenAuth as tokenAuth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Logins")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return tokenAuth.varify_token(token,credentials_exception)
    # try:
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #     username: str = payload.get("sub")
    #     if username is None:
    #         raise credentials_exception
    #     token_data = TokenData(username=username)
    # except JWTError:
    #     raise credentials_exception
    # user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    # return user
    