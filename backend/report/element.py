from backend.report.report import Report


class Element:
    """ Elements are smallest part of report holding data."""

    element_value_types = {"string", "decimal", "integer"}

    def __init__(self, name: str, value_type : str):
        self.name = name
        self.value_type = value_type
        self.period_values = {}  # period:value
        self.topics = set()  # set is changed via topic
        self.reports = set() # Set is changed via report

    def add_period_value(self, period: int, value):
        """periods: current reporting period 0, previous period -1, ..."""
        self.period_values[period] = value

    def add_report(self, report: Report):
        """Add reference to report that use element"""
        self.reports.add(report)

    def remove_report(self, report: Report):
        """Remove reference to report"""
        self.reports.remove(report)


