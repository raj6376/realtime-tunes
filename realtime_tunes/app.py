import os
import time
from redis_auth import hello_redis




start = time.time()

print(start)

if __name__ == '__main__':
    hello_redis("msg:hello")
    # msg = redis_conn.get("msg:hello")
    
    
