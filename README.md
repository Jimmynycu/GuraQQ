# GuraQQ

GuraQQ is a Python-based project designed to analyze YouTube comments on VTuber videos. It uses the YouTube Data API to fetch comments, performs sentiment analysis, extracts keywords, and builds a social interaction network among commenters.

## Features
- Fetch YouTube comments using the YouTube Data API.
- Perform sentiment analysis using Hugging Face's Transformers.
- Extract keywords using TF-IDF.
- Build and visualize a social interaction network.
- Generate sentiment distribution and keyword cloud visualizations.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Jimmynycu/GuraQQ.git
   cd GuraQQ
   ```

2. Install required Python packages:
   ```bash
   pip install google-api-python-client transformers torch networkx matplotlib seaborn wordcloud scikit-learn
   ```

3. (Optional) If using Google Colab, mount your Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. Replace the placeholders in the code with your API key and YouTube video ID:
   ```python
   API_KEY = 'your_api_key_here'
   VIDEO_ID = 'your_video_id_here'
   ```

## Usage
1. Open the `GuraQQ.ipynb` notebook in Jupyter or Google Colab.
2. Run the cells step by step to:
   - Fetch YouTube comments.
   - Perform sentiment analysis and keyword extraction.
   - Build and visualize the social interaction network.
   - Save results (e.g., CSV files, visualizations) to your Google Drive.

## Outputs
- **Sentiment Distribution**: A bar chart showing the distribution of sentiments in the comments.
- **Keyword Cloud**: A word cloud of the most important keywords in the comments.
- **Interaction Network**: A graph visualizing the social interactions among commenters.
- **Top Influencers**: A list of the top 5 influencers based on PageRank.
- **Community Detection**: The number of detected communities in the interaction network.

## License
This project is licensed under the MIT License. See the LICENSE file for details.