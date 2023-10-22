from .BaseObject import BaseObject

class Balance(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.limit = int(kwargs['monthly']['limit'])
        self.usage = int(kwargs['monthly']['usage'])
        self.balance = int(kwargs['prepaid']['balance'])
        # warning is set at 80% limit
        self.warning = self.usage >= self.limit * 0.8

        super(Balance, self).__init__(*args, **kwargs)