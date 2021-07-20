from datetime import datetime

class Toolbox():

    def __init__(self, tool_id, name, type, description, brand, cost, pieces, date_of_purchase, secondhand, imagedir):

        '''
        creating class instance variables
        '''
        self.tool_id = tool_id    #pk
        self.name = name    #what is the tool commonly called?
        self.type = type    #what type of tool is it? hand/power/diagnostic
        self.description = description    #
        self.brand = brand    #manufacturer of the tool
        self.cost = cost    #how much I paid for the tool
        self.pieces = pieces    #how many pieces in the set
        self.imagedir = imagedir    #string for image location

        '''
        convert boolean value into pre-determined string
        '''

        if secondhand == True:
            self.secondhand = 'Yes - Bargain!'
        elif secondhand == False:
            self.secondhand = 'No'

        '''
        convert string to datetime, save as class instance variable
        error checking in case of value error / incorrect string formatting
        '''
        try:
            self.date_of_purchase = datetime.strptime(date_of_purchase, "%d-%m-%Y").date()
        except ValueError:
            self.date_of_purchase = 'input error'
            print("time data does not match format %d-%m-%Y")
