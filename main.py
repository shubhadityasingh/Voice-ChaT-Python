from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

ip = socket.gethostbyname(socket.gethostname())

receiver = AudioReceiver(ip, 9999)
receive_thread = threading.Thread(target=receiver.start_server)