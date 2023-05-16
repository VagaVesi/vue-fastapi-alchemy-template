from backend.report.element import Element


class Topic:
    """Topics are areas to group elements"""

    def __init__(self, topic_name:str):
        self.topic_name = topic_name
        self.elements = set()

    def add_element(self, element: Element):
        """Make relation between topic and element"""
        pass

    def remove_element(self, element: Element):
        """Remove relation between topic and element"""
        pass

