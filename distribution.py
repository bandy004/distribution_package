class Distribution():

    def __init__(self) -> None:
        ''' This class represents a probability distribution.

        Attributes:
        data : Array that hold data
        mean : Mean of the distribution
        stddev: Standard deviation of the distribution

        Methods:
        calc_mean : calculate mean from the data
        calc_stddev: calculate standard deviation from the data 
        '''
        self.data = []
        self.mean = 0.0
        self.stddev = 0.0

    def calc_mean(self):
        return self.mean

    def calc_stddev(self):
        return self.stddev
