class Reference:
    """References to standards or regulations"""

    predefined_names = {'IFRS', 'RPS', 'ÄS'}

    def __init__(self, name, number, issue_date, section, paragraph, sub_paragraph, clause, sub_clause, uri, uri_date):
        self.name = name
        self.number = number
        self.issue_date = issue_date
        self.section = section
        self.paragraph = paragraph
        self.sub_paragraph = sub_paragraph
        self.clause = clause
        self.sub_clause = sub_clause
        self.uri = uri
        self.uri_date = uri_date

