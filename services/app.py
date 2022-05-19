import time
from aiohttp import web
from aiohttp.web_request import Request
import json
import asyncio
from authorization.conn import *


start = time.time()
print(start)

async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj), status=200)

async def hello(request):
    message = 'Hello World !!!'
    return web.Response(text=json.dumps(message), status=200)




async def redis(request):
    try:
        response_obj = redis_conn()
        return web.Response(response_obj, status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'message': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)






if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/hello-world', hello)
    app.router.add_get('/realtime_tunes', redis)
    web.run_app(app, host='0.0.0.0', port=80)


    # hello_redis("msg:hello")
    # msg = redis_conn.get("msg:hello")
