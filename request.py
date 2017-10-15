from urllib.parse import urlparse, unquote, parse_qs

class Request:
	def __init__(self, raw_request):
		self.method = self.__get_method(raw_request)
		self.headers = self.__get_headers(raw_request)
		self.host = self.headers.get('Host', '')
		self.url, self.path, self.query_params = self.__parse_url(raw_request)
		try:
			self.data = raw_request.split(b'\r\n\r\n')[1]
		except:
			self.data = ''

	def __parse_url(self, raw_request):
		raw_url = self.host + raw_request.split(b' ')[1].decode()
		if '://' not in raw_url:
			raw_url = '//' + raw_url
		parsed_url = urlparse(raw_url)
		return parsed_url.geturl(), unquote(parsed_url.path), parse_qs(unquote(parsed_url.query))

	def __get_method(self, raw_request):
		return raw_request.split(b' ')[0].decode()

	def __get_headers(self, raw_request):
		headers = raw_request.split(b'\r\n\r\n')[0]
		headers = headers.split(b'\r\n')[1:]
		headers_dict = {}
		for header in headers:
			header = header.decode().split(': ')
			headers_dict.update({header[0]: header[1]})
		return headers_dict