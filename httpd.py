import argparse
import configparser
import os
import socket

import sys

from server import MyHttpServer
from settings import *


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--host', default=DEFAULT_HOST, help='Host')
	parser.add_argument(
		'-p', '--port', default=DEFAULT_PORT, help='Port')
	parser.add_argument(
		'-l', '--listeners', default=DEFAULT_LISTENERS, help='Listeners')
	parser.add_argument(
		'-s', '--size', default=DEFAULT_RECV_MSG_SIZE, help='Recv msg size')
	parser.add_argument(
		'-r', '--root', default=DEFAULT_ROOT_DIR, help='Root directory for reading files')
	parser.add_argument(
		'-n', '--ncpu', default=3, type=int, help='Number of cpu')

	return parser.parse_args()


if __name__ == "__main__":
	args = parse_arguments()

	if not os.path.exists(args.root):
		print("Please, check root directory.")
		sys.exit()

	server = MyHttpServer(args.root, args.host, int(args.port), 
		int(args.ncpu), int(args.listeners), int(args.size))
	server.start()