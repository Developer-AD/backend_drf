from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.exceptions import # Close Consumer.
import time
import asyncio

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('-'*100)
        print('WEBSOCKET - CONNECT')
        print('-'*100)
        self.send({
            "type": "websocket.accept",
        })


    def websocket_receive(self, event):
        print('-'*100)
        print('WEBSOCKET - CONNECT')
        print(f"Event - Data : {event}")
        print('-'*100)

        
        # text_data_json = json.loads(text_data)
        # name = text_data_json.get("name")
        message = f"Hello {event.get('text')}, Good morning."

        print('-'*100)
        for i in range(1, 21):    
            self.send({
                "type": "websocket.send",
                "text": str(i),
                # "text": event["text"],
            })
            time.sleep(1)

    def websocket_disconnect(self, close_code):
        print('*'*100)
        print('WEBSOCKET - DISCONNECT')
        print('*'*100)
        pass

# ---------------------------- ASYNC CONSUMER ---------------------------.
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('-'*100)
        print('Async - WEBSOCKET - CONNECT')
        print('-'*100)
        await self.send({
            "type": "websocket.accept",
        })


    async def websocket_receive(self, event):
        print('-'*100)
        print('Async - WEBSOCKET - CONNECT')
        print(f"Event - Data : {event}")
        print('-'*100)
        
        # text_data_json = json.loads(text_data)
        # name = text_data_json.get("name")
        message = f"Hello {event.get('text')}, Good morning."

        print('-'*100)
        for i in range(1, 21):    
            await self.send({
                "type": "websocket.send",
                "text": str(i),
                # "text": event["text"],
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, close_code):
        print('*'*100)
        print('Async - WEBSOCKET - DISCONNECT')
        print('*'*100)
        pass


# ===============================================================
# import json

# from channels.generic.websocket import WebsocketConsumer
# from channels.exceptions import 


# class MySyncConsumer(WebsocketConsumer):
#     def connect(self):
#         print('-'*100)
#         print('WEBSOCKET - CONNECT')
#         print('-'*100)
#         self.accept()

#     def disconnect(self, close_code):
#         print('*'*100)
#         print('WEBSOCKET - DISCONNECT')
#         print('*'*100)
#         pass

#     def receive(self, text_data):
#         print('-'*100)
#         print('WEBSOCKET - CONNECT')
#         print(f"Text - Data : {text_data}")
#         print('-'*100)
        
#         # text_data_json = json.loads(text_data)
#         # name = text_data_json.get("name")
#         message = f"Hello {text_data}, Good morning."

#         # if name:
#         #     message = f"Hello {name}, Good morning."
#         # else:
#         #     message = f"Hello Annonymous, Good morning."
#         # message = text_data_json["message"]

#         print('-'*100)
#         self.send(text_data=json.dumps({"message": message}))