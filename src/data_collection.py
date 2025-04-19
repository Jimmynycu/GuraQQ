from googleapiclient.discovery import build
import pandas as pd

def get_youtube_comments(video_id, api_key, max_comments=100):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments.append({'author': author, 'comment': comment})

        next_page_token = response.get('nextPageToken')
        if not next_page_token or len(comments) >= max_comments:
            break

    return pd.DataFrame(comments)
