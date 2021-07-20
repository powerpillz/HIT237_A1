class Datamodel():

    def __init__(self, id, name, type, size, constraints, description, example):
        
        '''
        creating class instance variables for creation of data dictionary for Toolbox() variables
        '''
        self.id = id    #pk
        self.name = name    #name of toolbox class variable
        self.type = type    #data type
        self.size = size    #size/length
        self. constraints = constraints    #data constraint
        self.description = description    #description of Toolbox() class variable
        self.example = example    #example of Toolbox() class variable
