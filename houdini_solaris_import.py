# This code is a showcase of a second portfolio piece found in my technical artist portfolio found in:
# https://www.youtube.com/watch?v=vnzJ9yd-7wA
#This houdini script is used in the HDA settings. It allows to import files named as "piecex" when x is row of number.
#the code is for importing the pieces which are created as SOP in Houdini,
#however by changing sop_import the code is able to import files from the computer.

def importAll(parent):

    children = parent.children()
    for child in children:
        child.destroy()

    lop_merge = parent.createNode("merge")
    material_lib = parent.createNode("materiallibrary")
    material_lib.parm("materials").set('11')
    configure = parent.createNode("configureprimitive")
    setkind = configure.parm("setkind").set(True)
    kind = configure.parm("kind").set("subcomponent")
    sop_path = parent.evalParm("sop_path")
    num_items = parent.evalParm("num_of_items")


    material_lib.setInput(0, configure, 0)
    configure.setInput(0, lop_merge, 0)

    for number in range(int(num_items)):
        piece = str(number)
        sop_import_node = parent.createNode("sopimport", "piece"+piece)
        sop_parm = sop_import_node.parm("soppath")
        sop_parm.set(str(sop_path)+piece)
        sop_import_node.parm("asreference").set(True)
        sop_import_node.parm("primpath").set("/Scene/books")
        sop_import_node.parm("parentprimkind").set('group')
        sop_import_node.parm("enable_subsetgroups").set(True)
        sop_import_node.parm("subsetgroups").set("*")
        lop_merge.setNextInput(sop_import_node)

    for number in range(11):
        piece = str(number+1)
        material_lib.parm("matnode"+piece).set("/mat/book"+piece+"_MAT")
        material_lib.parm("matpath"+piece).set("/materials/book"+piece)
        material_lib.parm("geopath"+piece).set("/Scene/books/piece*/book"+piece)

    material_lib.setDisplayFlag(True)
