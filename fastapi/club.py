from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# class based dependency injection-

# class AuthService:
#     def verify_membership(Self, token: str):
#         if token == "vip_pass":
#             return True
#         else:
#             raise HTTPException(status_code=403, detail='forbidden')

# def get_auth_service():
#     return AuthService()

# auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]

# @app.get("/launge")
# def launge_access(token: str, auth_service: auth_service_dependency):
#     if auth_service.verify_membership(token):
#         return {"access to vip launge is approved"}

#----

# function based dependency injection
def verify_membership(token: str):
    if token == "vip_pass":
        return True
    else:
        raise HTTPException(status_code=403, detail="forbidden")
    
membership_dependency = Annotated[bool, Depends(verify_membership)]

@app.get("/lounge")
def launge_access(membership: membership_dependency):
    return {"message": "Access to VIP lounge is approved"}
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)