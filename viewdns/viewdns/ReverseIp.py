from .BaseObject import BaseObject

class ReverseIp(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.name = None
        self.last_resolved = None

        super(ReverseIp, self).__init__(*args, **kwargs)
