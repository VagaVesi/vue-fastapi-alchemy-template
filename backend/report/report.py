from backend.report.element import Element


class Report:
    """Report is ordered list of elements."""

    def __init__(self, report_name: str, period: str):
        self.report_name = report_name
        self.periods = {0: period}
        self.elements = []

    def add_element(self, position: int, element: Element):
        """Insert element to report position"""
        # add element to report
        if element in self.elements:
            raise ValueError('Element already used in report')
        if position not in range(0, len(self.elements)):
            self.elements.append(element)
        else:
            self.elements.insert(position, element)
        # Join report with element
        element.add_report(self)

    def add_period(self, period_key: int, period: str):
        """Add additional period to report"""
        self.periods[period_key] = period

    def delete_element(self, element):
        """Delete element from list"""
        self.elements.remove(element)
        element.remove_report(self)

    def get_elements(self) -> dict:
        """Return report elements with index"""
        result = {}
        for i in range(len(self.elements)):
            result[i] = self.elements[i]
        return result




