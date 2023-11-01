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
        self.send({
            'type': 'websocket.send',
            'text': 'Message is Sended'
        }) 

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
        await self.send({
            'type': 'websocket.send',
            'text': 'Message is Sended'
        }) 

    async def websocket_disconnect(self, event):
        print('Websocket is Disconnected....', event) 
        raise StopConsumer      