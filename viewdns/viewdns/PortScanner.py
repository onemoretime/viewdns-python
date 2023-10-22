from .BaseObject import BaseObject

class PortScanner(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.number = None
        self.service = None
        self.status = None

        super(PortScanner, self).__init__(*args, **kwargs)
