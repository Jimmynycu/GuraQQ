import networkx as nx
import numpy as np
from collections import defaultdict

def build_interaction_network(authors, interaction_probability):
    G = nx.Graph()
    for author in authors:
        G.add_node(author)

    np.random.seed(42)
    for i, author1 in enumerate(authors):
        for author2 in authors[i+1:]:
            if np.random.rand() < interaction_probability:
                G.add_edge(author1, author2)

    return G

def analyze_network(G):
    pagerank = nx.pagerank(G)
    top_influencers = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]
    communities = nx.algorithms.community.greedy_modularity_communities(G)
    community_dict = {node: i for i, comm in enumerate(communities) for node in comm}
    return top_influencers, community_dict
