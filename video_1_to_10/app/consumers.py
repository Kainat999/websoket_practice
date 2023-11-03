import asyncio
from time import sleep
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket is Connected', event)
        self.send({
            'type': 'websocket.accept',
        })


    def websocket_receive(self, event):
        print('Message is received........', event)   
        print(event['text'])
        for i in range(10):
            self.send({
            'type': 'websocket.send',
            'text': str(i)
        }) 
            sleep(1)

    def websocket_disconnect(self, event):
        print('Websocket is Disconnected....', event) 
        raise StopConsumer  
    



class TestAyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket is Connected', event)
        await self.send({
            'type': 'websocket.accept',
        })


    async def websocket_receive(self, event):
        print('Message is received........', event)   
        print(event['text'])
        for i in range(10):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
                })
            await asyncio.sleep(i) 

    async def websocket_disconnect(self, event):
        print('Websocket is Disconnected....', event) 
        raise StopConsumer      