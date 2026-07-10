def get_state_key(key: str):
    return f"user:{key}:state"

def get_data_key(key: str):
    return f"user:{key}:data"

def get_status_key(key: str):
    return f"user:{key}:status"
