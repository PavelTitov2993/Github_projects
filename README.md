# Github_projects

Hello to everyone who looks at my projects!

I've collected different scripts and tasks that I've done during my learning and further applying of Python.

Next I will list all of them with some description.

1. Honest_calc.py
This is an interactive calculator. We can perform all of the basic calculations and the ability to save the last result in the memory is also presented.
Writing this was a good practice of defining functions and using conditional operators.

2. main.py
This script helps to divide a check between a group of people, for example in restaraunt. There is also a "who is lucky" feature. It allows to randomly select one person
from the group, so he won't have to pay for (him/her)self and the bill will be split among the rest of them.

3. materials.ipynb
This is a more complicated case. My last place of work was engineering company that designs nuclear power plants. One of my responsibilities at that position was to
perform calculations of the reactor active zone under different loads and conditions. One particular case was modelling of melt benavior in the active zone during severe
accident. For such calculations we used highly specific software that is pretty demanding in terms of input data and its format.
So first I draw the axisymmetric model of reactor core in CAD software - like ANSYS, Pointwise etc. Next, this model was meshed, but the default format of mesh wasn't
compatible with final software. Apart from that, I should have divided the model to different zones - areas corresponding to different materials (steel, filler blocks etc.).
Every cell of my mesh had the "boundary condition" (BC) feature - number could be assigned to it to indicate what material it has. So I assembled major areas in the CAD
software and then divided then into lesser parts in script. To do this I've written 2 functions that redefine cell's number depending on its coordinates and BC.

Therefore I had to deal with 3 problems:

    1) Mesh format. I needed to write script to transform the data to appropriate form.
    
    2) Also, some physics aspects should be mentioned. In this task melt is located on the definite elevation, and then, 
    after the structural components are melted, it falls to the bottom of the vessel. So, obviously, filling of the reactor 
    vessel with melt goes from bottom to top. To take this into account mesh cells should be numerated - from bottom to top, 
    from axis to the wall. I failed to do that in CAD software, so I decided to include renumeration in my script.
    
    3) "Drawing" of the minor areas within the major ones.
    
In summary, this script receives the geometrical model in the form of 2 files - one with information about calculational cells (their numbers, numbers of the nodes they
consist of, and BC) and another with description of the nodes (their numbers and coordinates). Then all of the cells are renumerated. After that I define functions to
assign new BC and draw whatever I need. And finally I write all data to the new files in required format.

I added comments to the every part of this script for it to be more clear.

Feel free to ask me any details!
