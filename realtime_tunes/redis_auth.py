import json
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis(key):
    try:
        redis_conn = redis.StrictRedis(
            host=redis_host, 
            port=redis_port, 
            password=redis_password, 
            decode_responses=True
            )
        # print conn
        redis_conn.ping()
        print('Connected Successfully !')

        # r.set("msg:hello", "Hello Redis!!!")
        # redis_conn.set('realtime_tunes', '{"partner": "Tesla","region": {"id": "us-west-b"},"item-paging": "0001"}')
        # Retrieve the hello message from Redis
        msg = redis_conn.get(key)
        print(msg)        
    except Exception as ex:
        print('Error Details :', ex)
        exit('Failed to connect, Terminating...')


















'''
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from RealTime Tunes!')
    }

'''