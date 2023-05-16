class Schema:

    def __init__(self, schema_name):
        self.name = schema_name
        self.elements = {}
        self.labels = {}
        self.reference = {}
        self.definitions = {}
        self.calculations = {}
        self.enumerations = {}
