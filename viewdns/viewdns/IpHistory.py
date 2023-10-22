from .BaseObject import BaseObject

class IpHistory(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.ip = None
        self.owner = None
        self.location = None
        self.lastseen = None

        super(IpHistory, self).__init__(*args, **kwargs)
