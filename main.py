from src.config import CONFIG
from src.data_collection import get_youtube_comments
from src.nlp_analysis import analyze_sentiment, extract_keywords
from src.network_analysis import build_interaction_network, analyze_network
from src.visualization import plot_sentiment_distribution, plot_keyword_cloud, plot_interaction_network

def main():
    # Step 1: Collect data
    comments = get_youtube_comments(CONFIG['VIDEO_ID'], CONFIG['API_KEY'], CONFIG['MAX_COMMENTS'])
    comments.to_csv(f"{CONFIG['OUTPUT_DIR']}/vtuber_comments.csv", index=False)

    # Step 2: NLP Analysis
    comments = analyze_sentiment(comments, CONFIG['SENTIMENT_MODEL'])
    keywords = extract_keywords(comments, CONFIG['TFIDF_MAX_FEATURES'])

    # Step 3: Network Analysis
    G = build_interaction_network(comments['author'].unique(), CONFIG['INTERACTION_PROBABILITY'])
    top_influencers, community_dict = analyze_network(G)

    # Step 4: Visualization
    plot_sentiment_distribution(comments, CONFIG['OUTPUT_DIR'])
    plot_keyword_cloud(keywords, CONFIG['OUTPUT_DIR'])
    plot_interaction_network(G, community_dict, CONFIG['OUTPUT_DIR'])

    # Print results
    print("Top 5 Influencers (PageRank):")
    for influencer, score in top_influencers:
        print(f"{influencer}: {score:.4f}")
    print(f"Number of Communities: {len(set(community_dict.values()))}")

if __name__ == "__main__":
    main()
