from .BaseObject import BaseObject

class FreeEmail(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.provide_free_email = not 'DOES NOT' in kwargs['result']

        super(FreeEmail, self).__init__(*args, **kwargs)