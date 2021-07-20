from django.shortcuts import render
from .toolbox import Toolbox
from .datamodel import Datamodel

def navi(request):
    '''
    url(r'^navi/?$', views.navi, name='navi'),
    '''
    return render(request, 'BeamishA1_app/navi.html')       #combines template with context(none avail), and returns a http response object.

def home(request):
    '''
    url(r'^$', views.home, name='home'),
    '''
    datatopics = ["Name", "Description", "Brand", "Cost", "# Pieces", "Date of purchase", "New or secondhand", "Image Directory"]       #list for formatting in home template
    context_data = {
    'datatopics': datatopics,
    }
    return render(request, 'BeamishA1_app/home.html', context_data)       #combines template with context(none avail), and returns a http response object.

def list(request):
    '''
    url(r'^list/?$', views.list, name='list'),
    '''
    tool_list = add_tools()         #function is ran and compiled into list
    context_data = {                #dictionary is created using list for context data
    'tool_list': tool_list,
    }
    return render(request, 'BeamishA1_app/list.html', context_data)     #combines template with context, and returns a http response object.

def tool(request, tool_id):
    '''
    url(r'^tool/(\d{1,4})/?$', views.tool, name='tool'),
    '''
    tool_id = int(tool_id)              #tool_id converted to integer
    tool_list = add_tools()             #function is ran and compiled into list
    tool = None                         #Default setting
    secondhand = None                   #Default setting
    date_of_purchase = None             #Default setting

    for item in tool_list:              #for each item in tool_list
        if item.tool_id == tool_id:     #check to ensure each item tool id == tool id
            tool = item                 #set tool to equal item

    context_data = {                    #dictionary is created using list for context data
    'tool': tool,
    }
    return render(request, 'BeamishA1_app/tool.html', context_data)     #combines template with context, and returns a http response object.

def add_tools():
    '''
    Toolbox()
    (tool_id, name, type, description, brand, cost, pieces, date_of_purchase, secondhand, imagedir)
    '''
    addTool_list = []       #create empty list to append

    addTool_list.append(Toolbox(0,"Metric Spanner Roll", "Hand Tools", "Metric ring open ended spanners, 10mm-19mm", "Snap-On", "600", 11, "15-05-2019", False, "/static/images/0.jpg"))
    addTool_list.append(Toolbox(1,"Hammer", "Hand Tools", "Ball-pein hammer 680gram", "Estwing", "80", 1, "05-03-2016", False, "/static/images/1.jpg"))
    addTool_list.append(Toolbox(2,"Drill", "Power Tool", "18v cordless power drill with 13mm chuck", "Milwaukee", "450", 1, "10-12-2018", False, "/static/images/2.jpg"))
    addTool_list.append(Toolbox(3,"Drill", "Power Tool", "14v Cordless Power Drill with 9.5mm chuck", "Snap-On", "400", 1, "22-07-2016", False, "/static/images/3.jpg"))
    addTool_list.append(Toolbox(4,"Ratchet", "Hand Tools", "3/8 long handled ratchet with flex head and soft grip", "Snap-On", "10", 1, "11-02-2010", True, "/static/images/4.jpg"))
    addTool_list.append(Toolbox(5,"Ratchet", "Hand Tools", "3/8 stubby ratchet", "Snap-On", "300", 1, "01-02-2015", False, "/static/images/5.jpg"))
    addTool_list.append(Toolbox(6,"Thermal Camera", "Diagnostic Tools", "Thermal camera in hard case with 8gb sd card", "Snap-On", "2000", 3, "13-07-2018", False, "/static/images/6.jpg"))
    addTool_list.append(Toolbox(7,"Multi Meter", "Electrical Tools", "179 series true RMS digital multimeter", "Fluke", "200", 1, "10-06-2008", True, "/static/images/7.jpg"))
    addTool_list.append(Toolbox(8,"Test Light", "Electrical Tools", "Digital test light with volt-meter and polarity detection", "Snap-On", "150", 11, "11-09-2018", False, "/static/images/8.jpg"))
    addTool_list.append(Toolbox(9,"Deutsch Pins", "Consumable", "Male pins to suit 4mm wire", "OEX", "100", 100, "02-12-2019", False, "/static/images/9.jpg"))

    return addTool_list

def data(request):
    '''
    url(r'^data/?$', views.data, name='data'),
    '''
    dict_list = add_data()      #function is ran and compiled into list
    context_data = {            #dictionary is created using list for context data
    'dict_list': dict_list,
    }
    return render(request, 'BeamishA1_app/data.html', context_data)     #combines template with context, and returns a http response object.

def add_data():
    '''
    Datamodel()
    (id, name, type, size, constraints, description, example)
    '''
    addDict_list = []               #create empty list to append

    addDict_list.append(Datamodel(0, "tool_id", "Integer", "6", "Primary Key", "Unique identifier for each tool", "012345"))
    addDict_list.append(Datamodel(1, "name", "String", "25", "Not Null", "Name tool is commonly known as", "Hammer"))
    addDict_list.append(Datamodel(2, "type", "String", "25", "Not Null", "General classification of the tool", "Hand Tool"))
    addDict_list.append(Datamodel(3, "description", "String", "50", "Not Null", "Unique characteristics of the tool", "Ball-pein hammer 680gram"))
    addDict_list.append(Datamodel(4, "brand", "String", "25", "Not Null", "Manufacturer of the tool", "Estwing"))
    addDict_list.append(Datamodel(5, "cost", "String", "10", "Not Null", "How much I paid for the tool", "$80"))
    addDict_list.append(Datamodel(6, "pieces", "String", "3", "Not Null", "How many pieces in the kit", "1"))
    addDict_list.append(Datamodel(7, "date_of_purchase", "Floating Point", "10", "Default", "Date I purchased the tool", "05-10-2015"))
    addDict_list.append(Datamodel(8, "secondhand", "Boolean", "2", "Default", "Did I purchase the tool secondhand?", "False"))
    addDict_list.append(Datamodel(9, "imagedir", "URL", "30", "Validated", "Correct image directory or URL", "/static/images/1.jpg"))

    return addDict_list
