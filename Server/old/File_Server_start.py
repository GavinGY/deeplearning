import File_Server  
import threading  
import socketserver  
import time  
  
serverIp = '127.0.0.1'  
serverPort = 19821  
serverAddr = (serverIp,serverPort)  
  
class fileServerth(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
        self.create_time = time.time()  
        self.local = threading.local()  
  
    def run(self):  
        print("fileServer is running...")  
        fileserver.serve_forever()  
  
fileserver = socketserver.ThreadingTCPServer(serverAddr, File_Server.fileServer)  
fileserverth = fileServerth()  
fileserverth.start()  