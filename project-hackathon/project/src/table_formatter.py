"""Format data into ASCII tables."""

class TableFormatter:
    @staticmethod
    def create_table(headers, data):
        """Create a simple ASCII table."""
        # Calculate column widths
        widths = [len(str(header)) for header in headers]
        for row in data:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))
        
        # Create separator line
        separator = '+' + '+'.join('-' * (w + 2) for w in widths) + '+'
        
        # Create header
        result = [separator]
        header_row = '|' + '|'.join(f' {h:<{w}} ' for h, w in zip(headers, widths)) + '|'
        result.append(header_row)
        result.append(separator)
        
        # Create data rows
        for row in data:
            data_row = '|' + '|'.join(f' {str(c):<{w}} ' for c, w in zip(row, widths)) + '|'
            result.append(data_row)
        
        result.append(separator)
        return '\n'.join(result)