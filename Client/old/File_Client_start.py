import File_Client  
  
serverIp = '127.0.0.1'  
serverPort = 19821  
serverAddr = (serverIp,serverPort)  
  
fileclient = File_Client.fileClient(serverAddr)  
fileclient.sendFile('D:\\hello.jpg','')  
#fileclient.recvFile('toClientPath/file','fromServerPath/file')  