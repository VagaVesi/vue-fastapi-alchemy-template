class ElementXBRLProperties:
    item_type = {'monetary', 'string', 'decimal', 'integer', 'date'}

    def __init__(self, element_id: str, item_type):
        self.element_id = element_id
        self.type = item_type
        self.namespace = None
        self.namespace_prefix = None
        self.abstract = True
        self.period_type = None
        self.balance = None
        self.xml_id = None
        self.start_date = None
        self.end_date = None