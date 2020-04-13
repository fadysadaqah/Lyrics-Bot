def get_cc(video_id):
    from youtube_transcript_api import YouTubeTranscriptApi
    srt= YouTubeTranscriptApi.get_transcript(video_id,languages=('en','ar'))
    if srt[0]["start"]>srt[5]["start"]:
        srt=srt[::-1]
    return srt
