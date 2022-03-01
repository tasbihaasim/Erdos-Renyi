from cmath import inf
import networkx as nx
import numpy
import matplotlib.pyplot as plt


def erdos_renyi(n, p):
    avg_clus = []
    apl = []
    avg_deg = []
    for _ in range(30):
        G = nx.erdos_renyi_graph(n, p)
        avg_clus.append(nx.average_clustering(G))
        if nx.is_connected(G):
            apl.append(nx.average_shortest_path_length(G))
        deg = [val for node,val in G.degree()]
        avg_deg.append(numpy.mean(deg))
    print("when n = ",n, "and when p = ", p, "average clutering is:", numpy.mean(avg_clus) )
    print("when n = ",n, "and when p = ", p,  "average path length is:", numpy.mean(apl))
    print("when n = ",n, "and when p = ", p,  "average degree is:", numpy.mean(avg_deg))
    plt.hist(deg)
    plt.ylabel("degree distribution")
    plt.show()

#run the code everytime for new configs
erdos_renyi(4500, 0.09)