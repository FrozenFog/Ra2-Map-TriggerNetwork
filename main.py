from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from MapFile import MapFile
import matplotlib.pyplot as plt
import networkx as nx
import iniclass


def main():
    data = iniclass.IniFile()
    path = "E:\\Program Files\\RedAlert2\\"
    name = "sov09u" + ".map"  # input("map name:")
    filename = path + name
    with open(filename, "r") as f:
        lines = f.readlines()
        data.ReadData(lines)
    fmap = MapFile()
    fmap.LoadFromIni(data)
    nodes = []
    links = []
    symbSize = 6
    fmap.Calculate()
    # i = 1
    signedNames = []
    for trigger in fmap.triggers.values():
        #node = opts.GraphNode(name=trigger.name, symbol_size=trigger.count, symbol="rect", value=trigger.count/3)

        if (trigger.name in signedNames):
            continue
        #     trigger.name = trigger.name + str(i)
        #     i += 1
        else:
            signedNames.append(trigger.name)
        node = {
            "name":trigger.id + "-" + trigger.name,
            "symbol":"rect",
            "symbolSize":trigger.count,
            "value":trigger.count/3
        }
        if trigger.Associated():
            #assolink = opts.GraphLink(source=fmap.GetNameFromID(trigger.associated), target=trigger.name,symbol="arrow")
            assolink = {
                "source":fmap.GetNameFromID(trigger.associated),
                "target":trigger.id + "-" + trigger.name,
                "symbol":"arrow"
            }
            links.append(assolink)
        if len(trigger.movedtriggers) > 0:
            for movedid in trigger.movedtriggers:
                #movlink = opts.GraphLink(source=trigger.name, target=fmap.GetNameFromID(movedid),symbol="arrow",
                                         #symbol_size=symbSize)
                movlink = {
                    "source":trigger.id + "-" + trigger.name,
                    "target":fmap.GetNameFromID(movedid),
                    "symbol":"arrow",
                    "symbol_size":symbSize
                }
                links.append(movlink)
        if len(trigger.setlocals) > 0:
            for localid in trigger.setlocals:
                #setlink = opts.GraphLink(source=trigger.name, target=fmap.GetVarFromID(localid),
                                         #linestyle_opts=opts.LineStyleOpts(type_="dashed"),symbol="arrow",
                                         #symbol_size=symbSize)
                setlink = {
                    "source":trigger.id + "-" + trigger.name,
                    "target":fmap.GetVarFromID(localid),
                    "symbol":"arrow",
                    "symbol_size":symbSize
                }
                links.append(setlink)
        if len(trigger.readlocals) > 0:
            for localid in trigger.readlocals:
                # readlink = opts.GraphLink(source=fmap.GetVarFromID(localid), target=trigger.name,
                #                           linestyle_opts=opts.LineStyleOpts(type_="dashed"), symbol="arrow",
                #                           symbol_size=symbSize)
                readlink = {
                    "source":fmap.GetVarFromID(localid),
                    "target":trigger.id + "-" + trigger.name,
                    "symbol":"arrow",
                    "symbol_size":symbSize
                }
                links.append(readlink)
        #if not trigger.Nothing():
        nodes.append(node)
    for local in fmap.localvar.values():
        #node = opts.GraphNode(name=local.varname, symbol_size=local.varcount, symbol="circle", value=local.varcount/3)
        node = {
            "name":local.varname,
            "symbol":"circle",
            "symbolSize":local.varcount,
            "value":local.varcount/3
        }
        nodes.append(node)
    print("nodes", len(nodes))
    print("links", len(links))
    #DrawWithNx(links, nodes)
    DrawWithPye(links, nodes, name)

def DrawWithNx(links, nodes):
    g = nx.DiGraph()
    g.clear()
    for node in nodes:
        g.add_node(node["name"])
    for link in links:
        g.add_edge(link["source"], link["target"])
    nx.draw(g)
    plt.savefig("1.png")


def DrawWithPye(links, nodes, name):
    graph = Graph(opts.InitOpts(width="1920px", height="1080px"))
    graph.add("Name: ", nodes, links, repulsion=8000, is_rotate_label=True)
    graph.set_global_opts(title_opts=opts.TitleOpts(title=name + " trigger network"))
    graph.render()

if __name__ == '__main__':
    main()





