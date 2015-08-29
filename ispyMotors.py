import socket

CONTROL_PORT = 8150
DEFAULT_IP = '10.10.1.1'

class Motors():
    LEFT = 1
    RIGHT = 2
    HEAD = 3

    FORWARD = 1
    BACK = 2
    STOP = 0

    def __init__(self, ip=DEFAULT_IP, port=CONTROL_PORT):
        self.is_connected = False
        self.ip = ip
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    def init_connection(self):
        print 'Connecting to', self.ip
        self.connection.connect((self.ip, self.port))
        self.connection.sendall('t1')
        self.is_connected = True
        print 'Connected'
    
    def moveForward(self):
        self.command(1,1)
        self.command(2,1)

    def moveBackward(self):
        self.command(1,2)
        self.command(2,2)
    
    def moveLeft(self):
        self.command(1,2)
        self.command(2,1)

    def moveRight(self):
        self.command(1,1)
        self.command(2,2)

    def moveHeadUp(self):
        self.command(3,1)

    def moveHeadDown(self):
        self.command(3,2)
        
    def stopAll():
        self.command(1,0)
        self.command(2,0)
        self.command(3,0)
        
    def command(self, motor, direction):
        try:
            self.connection.sendall('%i%i' % (motor, direction))
        except IOError:
            print "IOERROR"
            self.is_connected = False