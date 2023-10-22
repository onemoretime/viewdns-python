from .BaseObject import BaseObject

class ReverseDns(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.rdns = None

        super(ReverseDns, self).__init__(*args, **kwargs)
