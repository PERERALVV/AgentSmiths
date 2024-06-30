def individual_serial(todo) -> dict:
    return {
        "_id": str(todo["_id"]),
        "name": str(todo["name"]),
        "password": str(todo["password"])
    }
    
def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]

def emailCheck_serial(todo) -> dict:
    return {
        "email": todo["email"]
    }
    
def email_serial(todos) -> list:
    return [emailCheck_serial(todo) for todo in todos]


def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "password": item["password"],
        "organization": item["organization"],
        "role": item["role"],
        "name": item["name"],
        "username": item["username"],
        "contact": item["contact"],
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

