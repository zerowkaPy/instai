def user_id_to_key(sender_id: int):
    key = f"user:{sender_id}:state"
    return key
    
def key_to_user_id(key: str):
    user_id = key.split(":")[1]
    return user_id