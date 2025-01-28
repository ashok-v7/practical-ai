from youtube_transcript_api import YouTubeTranscriptApi

# Replace with a valid YouTube video ID
video_id = "_SwY6yWzW00"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)

#https://www.youtube.com/watch?v=_SwY6yWzW00