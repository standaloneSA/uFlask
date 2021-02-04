try:
  import usocket as socket
except:
  import socket

class Server():
  def __init__(self, address='0.0.0.0', port='80', queue=5):
    """
      Initializes a socket listener. 

      @param address - IP address to listen on. default 0.0.0.0
      @param port - TCP port to listen on. Default 80
      @param queue - socket queue size. Default of 5 (this is IOT not Google)
    """

    # Set up socket stuff
    ai = socket.getaddrinfo(address, port)
    self.addr = ai[0][-1]
    self.queue = queue

  def __repr__(self):
    return("%s:%s" % (self.addr[0],self.addr[1]))

  def _listen(self):
    while True:
      res = self.s.accept()
      client_sock = res[0]
      client_addr = res[1]
      print("Connection from %s:%s" % (client_addr, client_sock))
      client_stream = client_sock
      
      req = []
      while True:
        line = client_stream.readline()
        req.append(str(line))
        if line == b"" or line == b"\r\n":
          print("End of request.")
          break
      req = "\n".join(req)
      print("Request: %s" % req)
      client_stream.write("200 Okay, will work on that.")
      client_stream.close()
      print("---")

  def start(self):
    self.s = socket.socket()
    self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.s.bind(self.addr)
    self.s.listen(self.queue)
  
    print("Listening on %s" % str(self.addr))
    self._listen() 

  
    
