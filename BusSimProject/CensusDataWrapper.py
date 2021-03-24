import censusdata

class Census:
    
    def __init__(self, dataset, year):
        self.geodatafile = "shapes.csv"
        
        return 

    
# Pulling in setting the lat-lon data to be converted to counties list:

    def set_geodatafile(self, filename):
        self.geodatafile = filename
        return
    
    def get_geodatafile(self, filename):
        return self.geodatafile
    