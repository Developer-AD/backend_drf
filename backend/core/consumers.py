import json

from channels.generic.websocket import WebsocketConsumer


class MySyncConsumer(WebsocketConsumer):
    def connect(self):
        print('-'*100)
        print('WEBSOCKET - CONNECT')
        print('-'*100)
        self.accept()

    def disconnect(self, close_code):
        print('*'*100)
        print('WEBSOCKET - DISCONNECT')
        print('*'*100)
        pass

    def receive(self, text_data):
        print('-'*100)
        print('WEBSOCKET - CONNECT')
        print('-'*100)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))