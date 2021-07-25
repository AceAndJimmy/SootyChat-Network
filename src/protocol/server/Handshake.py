from ...Packet import Packet

class Handshake(Packet):

    def __init__(self):
        super().__init__()
    id = 2

    def unpack(self):
        pass

    def build(self):
        pass
