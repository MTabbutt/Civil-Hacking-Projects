import censusdata

class Census:
    
    def __init__(self, dataset, year):
        self.dataset = dataset
        self.year = year
        
        return 
        
    def getSummary(self):
        print("Dataset = ", self.dataset)
        print("Year = ", self.year)
        
        return
    
    
    def getStateCodes(self, state='*'):
        
        try:
            self.stateData = censusdata.geographies(censusdata.censusgeo([('state', '*')]), self.dataset, self.year)
            if state == '*':
                for key in self.stateData:
                    print(key, " : ", self.stateData[key])
            else:
                print(state, " : ", self.stateData[state])
            
        except:
            print("State was not found, use: getStateCodes(), to get a list of all states.")
    
        return 
    
    
    
    
    