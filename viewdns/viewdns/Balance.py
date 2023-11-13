from .BaseObject import BaseObject

class Balance(BaseObject):

    def __init__(self, *args, **kwargs):
        if 'monthly' in kwargs:
            # this is paid account
            self.limit = int(kwargs['monthly']['limit'])
            self.usage = int(kwargs['monthly']['usage'])
        elif 'trial' in kwargs:
            # this is a free/trial account
            self.limit = int(kwargs['trial']['limit'])
            self.usage = int(kwargs['trial']['usage']) 
        else:
            existing_keys = ",".join(list(kwargs.keys()))
            raise KeyError(f"Missing trial or prepaid key in response. Received Keys are {existing_keys}")
        self.balance = int(kwargs['prepaid']['balance'])
        # warning is set at 80% limit
        self.warning = self.usage >= self.limit * 0.8

        super(Balance, self).__init__(*args, **kwargs)