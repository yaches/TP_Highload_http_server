import os

from settings import DEFAULT_PAGE
from response import MyHttpResponse, ResponseCode, CONTENT_TYPES


class MyHttpRequestHandler:
	def __init__(self, request, root_dir):
		self.request = request
		self.root_dir = root_dir

	def handle(self):
		if not self.request.method in ["GET", "HEAD"]:
			response = MyHttpResponse(ResponseCode.NOT_ALLOWED)
		else:
			real_path = os.path.normpath(self.root_dir + '/' + self.request.path)
			response = MyHttpResponse(code=ResponseCode.NOT_FOUND)

			if os.path.commonprefix([real_path, self.root_dir]) != self.root_dir:
				return response

			if os.path.isfile(os.path.join(real_path, DEFAULT_PAGE)):
				real_path = os.path.join(real_path, DEFAULT_PAGE)
			elif os.path.exists(os.path.join(real_path)):
				response.code = ResponseCode.FORBIDDEN
			try:
				with open(real_path, 'rb') as fd:
					content = fd.read()
					response.body = content if self.request.method == 'GET' else b''
					response.content_length = len(content)
					response.content_type = self.__get_content_type(real_path)
					response.code = ResponseCode.OK
			except IOError:
				pass

		return response

	def __get_content_type(self, path):
		file_type = path.split('.')[-1]
		return CONTENT_TYPES.get(file_type, '')
		