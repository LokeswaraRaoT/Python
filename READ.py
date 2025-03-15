from abc import ABC, abstractmethod

class ReadFile(ABC):
    @abstractmethod
    def extract(self):
        pass

class ReadCSV(ReadFile):
    def extract(self):
        return "extract csv"
    
class ReadParquet(ReadFile):
    def extract(self):
        return "extract parquet"
    
read_csv = ReadCSV()
print(read_csv.extract())

read_par = ReadParquet()
print(read_par.extract())