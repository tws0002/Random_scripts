nuke.createNode("ColorWheel", "rotate 100")

nuke.createNode("Blur", "size 5")
nuke.createNode("Blur", "size {5, 10}")
cWheel = nuke.nodes.ColorWheel()

print cWheel

print cWheel.Class()
cWheel["rotate"].setValue(45)

print cWheel["rotate"].value()

const = nuke.selectedNode()

print const["name"].value()

const["color"].setValue([1,0,1,1])

nodes = nuke.allNodes("ColorWheel")
print "\n"
for node in nodes:
    print node["name"].value()

nodes = nuke.allNodes("Constant")
for node in nodes:
    node["color"].setValue([0,0,1,1])


constant = nuke.nodes.Constant()
wheel = nuke.nodes.ColorWheel()
merge = nuke.nodes.Merge2()

merge.setInput(1, wheel)
merge.setInput(0, constant)

print merge.xpos()
print merge.ypos()

merge.setXpos(150)