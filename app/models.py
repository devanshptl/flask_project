def usermodel(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }
