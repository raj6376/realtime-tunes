import asyncio
import asyncio_redis

key = 'msg:hello'

async def redis_conn():
    loop = asyncio.get_event_loop()

    # Create Redis connection
    transport, protocol = await loop.create_connection(
        asyncio_redis.RedisProtocol, 'localhost', 6379)

    # Set a key
    # await protocol.set('my_key', 'my_value')

    # Get a key
    result = await protocol.get(key)
    print(result)

    # Close transport when finished.
    transport.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(redis_conn())