class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()