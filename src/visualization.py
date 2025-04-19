import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import networkx as nx

def plot_sentiment_distribution(comments, output_dir):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=comments, x='sentiment')
    plt.title('Sentiment Distribution of VTuber Video Comments')
    plt.savefig(f"{output_dir}/sentiment_distribution.png")
    plt.show()

def plot_keyword_cloud(keywords, output_dir):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Top Keywords in Comments')
    plt.savefig(f"{output_dir}/keyword_cloud.png")
    plt.show()

def plot_interaction_network(G, community_dict, output_dir):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    node_colors = [community_dict.get(node, 0) for node in G.nodes()]
    nx.draw(G, pos, node_color=node_colors, node_size=50, cmap=plt.cm.Set3, with_labels=False)
    plt.title('VTuber Fan Interaction Network')
    plt.savefig(f"{output_dir}/network_graph.png")
    plt.show()
