import json
import typing as t 
from urllib import parse 

class State:
	CONNECTING = 1
	CONNECTED = 2
	DISCONNECTED = 3

class SendEvent:
	ACCEPT = "websocket.accept"
	SEND = "websocket.send"
	CLOSE = "websocket.close"

class ReceiveEvent:
	CONNECT = "websocket.connect"
	RECEIVE = "websocket.receive"
	DISCONNECT = "websocket.disconnect"

class Headers:
	def __init__(self, scope):
		self._scope = scope

	def keys(self):
		return [header[0].decode() for header in self._scope["headers"]]

	def as_dict(self) -> dict:
		return {h[0].decode(): h[1].decode() for h in self._scope["headers"]}

	def __getitem__(self, item:str) -> str:
		return self.as_dict()[item.lower()]

	def __repr__(self) -> str:
		return str(dict(self))

class QueryParams:
	def __init__(self, query_string: str):
		self._dict = dict(parse.parse_qsl(query_string))

	def keys(self):
		return self.as_dict.keys()

	def get(self, item, default=None):
		return self._dict.get(item, default)

	def __getitem__(self, item: str):
		return self._dict[item]

	def __repr__(self) -> str:
		return str(dict(self))


class WebSocket:
	def __init__(self, scope, receive, send):
		self._scope = scope
		self._receive = receive
		self._send = send 
		self._client_state = State.CONNECTING
		self._app_state = State.CONNECTING

	@property
	def Headers(self):
		return Headers(self._scope)

	@property
	def scheme(self):
		return self._scope["scheme"]

	@property
	def path(self):
		return self._scope["path"]

	@property
	def query_params(self):
		return QueryParams(self._scope["query_params"].decode())

	@property
	def query_string(self) -> str:
		return self._scope["query_params"]

	@property
	def scope(self):
		return self._scope

	async def accept(self, subprotocol: str = None):
		if self._client_state == State.CONNECTING:
			await self.receive()
		await self.send({"type": SendEvent.ACCEPT, "subprotocol": subprotocol})

	async def  close(self, code: int = 1000):
		await self.send({"type": SendEvent.CLOSE, "code": code})

	async def send(self, message: t.Mapping):
		if self._app_state == State.DISCONNECTED:
			raise RunTimeError("WebSocket is disconnected.")

		if self._app_state == State.CONNECTING:
			assert message["type"] in {SendEvent.ACCEPT, SendEvent.CLOSE}, ('No se pudo escribir el evento "%s" en el socket conectando el state.' % message["type"])
			if message["type"] == SendEvent.CLOSE:
				self._app_state = State.DISCONNECTED
			else:
				self._app_state = State.CONNECTED 

		elif self._app_state == State.CONNECTED:
			assert message["type"] in {SendEvent.SEND, SendEvent.CLOSE}, (
				'Socket conectado puede enviar "%s" eventos, no "%s"' % (SendEvent.SEND, SendEvent.CLOSE, message["type"])
			)
			if message["type"] == SendEvent.CLOSE:
				self._app_state = State.DISCONNECTED

		await self._send(message)

	async def receive(self):
		if self._client_state == State.DISCONNECTED:
			raise RunTimeError("WebSocket is disconnected.")

		message = await self._receive()

		if self._client_state == State.CONNECTING:
			assert message["type"] == ReceiveEvent.CONNECT, (
				'WebSocket esta conectado recibiendo "%s" evento' % message["type"]
			)
			self._scope = State.CONNECTED

		elif self._client_state == State.CONNECTED:
			assert message["type"] in {ReceiveEvent.RECEIVE, ReceiveEvent.DISCONNECt}, (
				'Websocket esta conectado pero recibe evento invalido "%s". ' % message["type"]
			)
			if message["type"] == ReceiveEvent.DISCONNECT:
				self._client_state = State.DISCONNECTED
		return message

	async def receive_json(self) -> t.Any:
		message = await self.receive()
		self._test_if_can_receive(message)
		return json.loads(message["text"])

	async def receive_jsonb(self) -> t.Any:
		message = await self.receive()
		self._test_if_can_receive(message)
		return json.loads(message["bytes"].decode())

	async def receive_text(self) -> str:
		message = await self.receive()
		self._test_if_can_receive(message)
		return message["text"]

	async def receive_bytes(self) -> str:
		message = await self.receive()
		self._test_if_can_receive(message)
		return message["bytes"]

	async def send_json(self, data: t.Any, **dump_kwargs): 
		data = json.dumps(data, **dump_kwargs)
		await self.send({"type": SendEvent.SEND, "text": data})

	async def send_jsonb(self, data: t.Any, **dump_kwargs): 
		data = json.dumps(data, **dump_kwargs)
		await self.send({"type": SendEvent.SEND, "bytes": data.encode()})

	async def send_text(self, text:str): 
		await self.send({"type": SendEvent.SEND, "text": text})

	async def send_bytes(self, text: t.Union[str, bytes]):
		if isinstance(text, str):
			text = text.encode()
		await self.send({"type": SendEvent.SEND, "bytes": text})

	def _test_if_can_receive(self, message: t.Mapping):
		assert message["type"] == ReceiveEvent.RECEIVE, (
			'Tipo de mensaje invalido "%s". Fue aceptada la conexion?' % message["type"]
		)


		



