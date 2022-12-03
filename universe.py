from system import System


class Universe:
    rows = 5
    columns = 6

    def __init__(self):
        self.universe = [[System() for columns in range(self.columns)] for rows in range(self.rows)]

