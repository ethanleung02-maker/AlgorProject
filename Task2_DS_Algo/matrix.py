class Matrix:
    """A simple Matrix data structure implemented using nested lists."""
    
    def __init__(self, rows, cols, default=0):
        """Initialize a matrix with given dimensions and default value."""
        self.rows = rows
        self.cols = cols
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def set_value(self, i, j, value):
        """Set the element at position (i, j) to 'value'."""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value
        else:
            raise IndexError("Matrix index out of range")

    def get_value(self, i, j):
        """Return the element at position (i, j)."""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            raise IndexError("Matrix index out of range")

    def transpose(self):
        """Return a new Matrix that is the transpose of this one."""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def display(self):
        """Pretty‑print the matrix row by row."""
        for row in self.data:
            print(row)

    def __str__(self):
        """Return string representation for debugging."""
        return "\n".join(str(row) for row in self.data)