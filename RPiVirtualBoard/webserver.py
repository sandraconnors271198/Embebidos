from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):
 	def do_GET(self):
 		self.send_response(200)
 		self.send_header("Content-type", "text/html")
 		self.end_headers()
 		self.wfile.write(bytes("<html><body>Hola Mundo!!!</body></html>", "utf-8"))

def main():
 	webServer = HTTPServer(("192.168.1.254", 80), WebServer)
 	print("Servidor iniciado")
 	print ("\tAtendiendo solicitudes entrantes")
 	try:
 		webServer.serve_forever()
 	except KeyboardInterrupt:
 		pass
 	webServer.server_close()
 	print("Server stopped.")

def do_GET(self):
 # Revisamos si se accede a la raiz.
 # En ese caso se responde con la interfaz por defecto
 	if self.path == '/':
 # 200 es el código de respuesta satisfactorio (OK)
 # de una solicitud
 		self.send_response(200)
 # La cabecera HTTP siempre debe contener el tipo de datos mime
 # del contenido con el que responde el servidor
 		self.send_header("Content-type", "text/html")
 # Fin de cabecera
 		self.end_headers()
 # Por simplicidad, se devuelve como respuesta el contenido del
 # archivo html con el código de la página de interfaz de usuario
 		self._serve_ui_file()
 # En caso contrario, se verifica que el archivo exista y se sirve
 	else:
 		self._serve_file(self.path[1:])

def _serve_file(self, rel_path):
	if not os.path.isfile(rel_path):
		self.send_error(404)
		return
	self.send_response(200)
	mime = magic.Magic(mime=True)
	self.send_header("Content-type", mime.from_file(rel_path))
	self.end_headers()
	with open(rel_path, 'rb') as file:
 		self.wfile.write(file.read())

def do_POST(self):
 # Primero se obtiene la longitud de la cadena de datos recibida
 	content_length = int(self.headers.get('Content-Length'))
 	if content_length < 1:
 		return
 # Después se lee toda la cadena de datos
 	post_data = self.rfile.read(content_length)
 # Finalmente, se decodifica el objeto JSON y se procesan los datos.
 # Se descartan cadenas de datos mal formados
 	try:
 		jobj = json.loads(post_data.decode("utf-8"))
 		self._parse_post(jobj)
 	except:
 		print(sys.exc_info())
 		print("Datos POST no recnocidos")

def _parse_post(self, json_obj):
	if not 'action' in json_obj or not 'value' in json_obj:
 		return
	switcher = {
 	'led' : leds,
 	'marquee' : marquee,
 	'numpad' : bcd
 	}
 	func=switcher.get(json_obj['action'],None )
 	if func:
 		print('\tCall{}({})'.format(func, json_obj['value']))
 		func(json_obj['value'])
