import asyncio
from aiocoap import Context, Message, CHANGED
import aiocoap.resource as resource

class SensorDataResource(resource.Resource):
    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        payload = request.payload.decode('utf-8')
        print(f"Received data: {payload}")
        return Message(code=CHANGED, payload=b'Data received')

async def main():
    root = resource.Site()
    root.add_resource(['sensor', 'data'], SensorDataResource())

    await Context.create_server_context(root, bind=('localhost', 5683))
    print("CoAP server running on coap://localhost:5683")
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
