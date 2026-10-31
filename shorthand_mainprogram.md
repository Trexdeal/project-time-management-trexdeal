this is for making notes 
I had to replace [] with () because I hated the blue colour
 #Datacreate consists of this structured type of list, (type of object (square, circle, (polygon, polygoncount),etc), size, relxy , (colour primary, line colour)(smaller list:interactable (truefalse), xsize, xdisplacement, ysize, ydisplacement ) ("multiobject", amount of this object, relxdistance between objects, relydistance between objects) nameobject) 
        #this list can consist of multiple objects at once, this is simply  the structure for 1 thing, consisting of 16 variables to help create any object required
        #if a polygon is chosen then 
        #if polygon then extra things will be added to show which 
        #rel stands for relative, to avoid issues with different screen sizes
        #colour 2 may go unused for certain shapes, in which case it will be identical to colour 1
        #The smaller list is used to pottentially define hitboxes, first part is just about if its interactable and will be false if it isn't, afterwards it will be possible to have x size, x displacement, y size and y displacement
        #nameobject will be changed if it is creating multiple objects, something similar to 
        #polygoncount optional
        #list unrolled:
            "is for clarification here
            (n(0)) = "type of object": rectangle, circle, (polygon, polygoncount)
                (n(0(2))) (polygon/polygoncount)
            (n(1)) = "size" (relativexsize/absx size, relysize/absy size)
            (n(2)) = "location" (relxloc/absx size, relyloc/absy size)
            (n(3)) = "colour" (primary colour, secondary colour)
            (n(4)) = "interactable"(true/false, xsize/"size"(0),xdispl/"size(0)", ysize/"size"(1), ydispl/"size"(1))
            (n(5)) = "multiobject", (nobject, relx/absx*1920, rely/absy*1080,), 
            (n(6)) = "name" #will be changed with multiobject
            (n(7)) = "canvas/location" (name of the canvas)
            (n(8)) = "image" (true/false, relsizex/1, relsiy/1,image name)




        