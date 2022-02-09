class Department:
    
    def __init__(self, max_people):
        
        self.personList = []

        self.max_people = max_people
    
    def add(self, name, phone):
        
        while True:
            if (len(self.personList)) < (self.max_people):
                self.personList.append({
                "name": name,
                "phone": phone
            })   
            else:
                break
            
        
    def __getitem__(self, name):

        for items in self.personList:
            if items["name"] == name:
                return name

    
    def getPeople(self):
           return self.personList