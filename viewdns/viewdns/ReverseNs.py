from .BaseObject import BaseObject

class ReverseNs(BaseObject):

    def __init__(self, *args, **kwargs):
        
        self.domain_count = None
        self.total_pages = None
        self.current_page = None
        self.domains = None

        super(ReverseNs, self).__init__(*args, **kwargs)
