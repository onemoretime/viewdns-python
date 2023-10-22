from .BaseObject import BaseObject

class MacLookup(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.manufacturer = None

        super(MacLookup, self).__init__(*args, **kwargs)
