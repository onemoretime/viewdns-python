from .BaseObject import BaseObject

class Ping(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.rtt = None

        super(Ping, self).__init__(*args, **kwargs)
