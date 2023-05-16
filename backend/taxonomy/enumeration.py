from backend.report.element import Element

"""Enumerated list of """


class Enumeration:

    def __init__(self, name: str):
        self.name = name
        self.enumeration_values = set()
        self.used_by_elements = set()

    def add_value(self, item: str):
        """Add new item to Extended Enumeration"""
        self.enumeration_values.add(item)

    def add_used_by_element(self, element: Element):
        """Add reference to element using this enumeration"""
        self.used_by_elements.add(element)