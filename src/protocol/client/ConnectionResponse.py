from ...Packet import Packet
import struct
class ConnectionResponse(Packet):

    def __init__(self) -> None:
        super().__init__()
    id = 1

    def unpack(self):
        self.id = struct.unpack(">b", self.id)
        return self.id

    def build(self):
        self.id = struct.pack(">b", self.id)
        return self.id
