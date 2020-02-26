from pyecharts import options as opts
from pyecharts.charts import Graph
# import matplotlib.pyplot as plt
# import networkx as nx
from MapFile import MapFile
import iniclass
import globalvar as g


def main(name):
    data = iniclass.IniFile()
    #path = "E:\\Program Files\\RedAlert2\\AllMap\\mapextract\\expand99\\"
    #name = "Epsilon A2 Mission Machinehead" + ".map"
    #filename = path + name
    with open(name, "r") as f:
        lines = f.readlines()
        data.ReadData(lines)
    fmap = MapFile()
    fmap.LoadFromIni(data)
    nodes = []
    links = []
    fmap.Calculate()
    # signedNames = []
    for trigger in fmap.triggers.values():
        # node = opts.GraphNode(name=trigger.name, symbol_size=trigger.count, symbol="rect", value=trigger.count/3)
        # if trigger.name == "New trigger":
        #     continue
        # if trigger.name in signedNames:
        #     trigger.name = trigger.name + str(i)
        #     i += 1
        # else:
        #     signedNames.append(trigger.name)
        node = {
            "name": trigger.id + "-" + trigger.name,
            "symbol": "rect",
            "symbolSize": trigger.count,
            "value": trigger.count / g.triggerInit
        }
        if trigger.Associated():
            # assolink = opts.GraphLink(source=fmap.GetNameFromID(trigger.associated), target=trigger.name,symbol="arrow")
            assolink = {
                "source": fmap.GetNameFromID(trigger.associated),
                "target": trigger.id + "-" + trigger.name
            }
            links.append(assolink)
        if len(trigger.movedtriggers) > 0:
            for movedid in trigger.movedtriggers:
                # movlink = opts.GraphLink(source=trigger.name, target=fmap.GetNameFromID(movedid),symbol="arrow",
                # symbol_size=symbSize)
                movlink = {
                    "source": trigger.id + "-" + trigger.name,
                    "target": fmap.GetNameFromID(movedid)
                }
                links.append(movlink)
        if len(trigger.setlocals) > 0:
            for localid in trigger.setlocals:
                # setlink = opts.GraphLink(source=trigger.name, target=fmap.GetVarFromID(localid),
                # linestyle_opts=opts.LineStyleOpts(type_="dashed"),symbol="arrow",
                # symbol_size=symbSize)
                setlink = {
                    "source": trigger.id + "-" + trigger.name,
                    "target": fmap.GetVarFromID(localid)
                }
                links.append(setlink)
        if len(trigger.readlocals) > 0:
            for localid in trigger.readlocals:
                # readlink = opts.GraphLink(source=fmap.GetVarFromID(localid), target=trigger.name,
                #                           linestyle_opts=opts.LineStyleOpts(type_="dashed"), symbol="arrow",
                #                           symbol_size=symbSize)
                readlink = {
                    "source": fmap.GetVarFromID(localid),
                    "target": trigger.id + "-" + trigger.name
                }
                links.append(readlink)
        # if not trigger.Nothing():
        if node["value"] > 1:
            nodes.append(node)
        elif not g.isolated:
            nodes.append(node)
    for local in fmap.localvar.values():
        # node = opts.GraphNode(name=local.varname, symbol_size=local.varcount, symbol="circle", value=local.varcount/3)
        node = {
            "name": "Local-" + local.varid + ":" + local.varname,
            "symbol": "circle",
            "symbolSize": local.varcount,
            "value": local.varcount / g.localInit
        }
        nodes.append(node)
    print("nodes", len(nodes))
    print("links", len(links))
    # DrawWithNx(links, nodes)
    DrawWithPye(links, nodes, name)


# def DrawWithNx(links, nodes):
#     g = nx.DiGraph()
#     g.clear()
#     for node in nodes:
#         g.add_node(node["name"])
#     for link in links:
#         g.add_edge(link["source"], link["target"])
#     nx.draw(g)
#     plt.savefig("1.png")


def DrawWithPye(links, nodes, name):
    graph = Graph(opts.InitOpts(width=g.w_s, height=g.h_s))
    graph.add("Node Name: ", nodes, links, repulsion=g.repul,
              label_opts=opts.LabelOpts(is_show=g.label), is_draggable=g.drag)
    graph.set_global_opts(title_opts=opts.TitleOpts(title=name + g.titleend))
    graph.render()


def SetGlobal(args):
    if "-l" in args:
        g.label = True
    if "-d" in args:
        g.drag = False
    if "-w" in args:
        g.width = int(args[args.index("-w") + 1])
    if "-h" in args:
        g.height = int(args[args.index("-h") + 1])
    if "-r" in args:
        g.repul = int(args[args.index("-r") + 1])
    if "-i" in args:
        g.isolated = True


if __name__ == '__main__':
    mapname = input("Map name(include \".map\")\nMust in same directory!(or full path if not):\n")
    args = input("""\n
Set parameters:
-w [width]\t\t\tSet graph width, default=1920
-h [height]\t\t\tSet graph height, default=1080
-r [repulsion]\t\tSet repulsion, default=8000
-l\t\t\t\t\tShow label on each node, default false
-d\t\t\t\t\tSet each note is NOT dragable, default true
-i\t\t\t\t\tIgnore isolated trigger, default false
\nLeave it empty will run with default params:\n""")
    SetGlobal(args.split(" "))
    main(mapname)
    print("Finished. Press enter to exit.")
    input("")
