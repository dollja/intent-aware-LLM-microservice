import redis
import json

redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

def save_session(user_id, data):
    redis_client.set(f"user_session:{user_id}", json.dumps(data))

def get_session(user_id):
    session_data = redis_client.get(f"user_session:{user_id}")
    return json.loads(session_data) if session_data else []