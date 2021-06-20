from os import name
import socketio
from camera_pi import Camera

def on_aaa_response(args):
	print('on_aaa_response', args['data'])

sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
	print("I'm connected!")
	sio.emit('aaa')

@sio.event
def connect_error(data):
	print("The connection failed!")
	exit()

@sio.event
def disconnect():
	print("I'm disconnected!")
	exit()


sio.connect('http://192.168.0.10:8000', namespaces='/test')	

camera = Camera()
while True:
	print("Frame")
	frame = camera.get_frame()
	sio.emit('frame', frame, '/test')
	
