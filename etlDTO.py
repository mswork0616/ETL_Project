
class EtlDTO:
    def __init__(self, newid, newtitle, newrelease_date, newruntime):
        self.id = newid    
        self.title = newtitle
        self.release_date = newrelease_date
        self.runtime = newruntime


    def getId(self):
        return self.id 

    def setId(self, newId):
        self.id = newId    

    def getTitle(self):
        return self.title
    
    def setTitle(self, newTitle):
        self.title = newTitle
    
    def getRelease_date(self):
        return self.release_date
    
    def setRelease_date(self, newRelease_date):
        self.release_date = newRelease_date
   
    def getRuntime(self):
        return self.runtime
    
    def setRuntime(self, newRuntime):
        self.runtime = newRuntime



    def __str__(self):
        return 'ID : ' + str(self.id) + ', 영화 제목 : ' + self.title + ', 개봉일 : ' + str(self.release_date) + ', 상영 시간 : ' + str(self.runtime)


