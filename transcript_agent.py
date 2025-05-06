import os
from textwrap import dedent
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools
from models import YouTubeTranscript

# Create the YouTube transcript agent with Agno's built-in YouTubeTools
transcript_agent = Agent(
    name="YouTube Transcript Agent",
    model=Gemini(
        id="gemini-2.5-flash-preview-04-17",
    ),
    tools=[YouTubeTools()],
    description=dedent(
        """\
        You are a YouTube transcript specialist who efficiently extracts and processes 
        video transcripts. Your job is to get clean, usable text from YouTube videos
        that can be used for creating blog content.
    """
    ),
    add_datetime_to_instructions=True,
    instructions=dedent(
        """\
        1. Extract the transcript from the provided YouTube URL
        2. Clean and process the transcript to make it more readable
        3. Identify the main topic and key points of the video
        4. Remove filler words, repetitions, and irrelevant content
        5. Format the transcript in a way that's suitable for blog post creation
        
        Keep the essential content intact while making the transcript more readable.
        Focus on maintaining the educational value and key insights from the video.
        
        After processing, output ONLY a raw JSON object with these exact keys: video_id, video_title, transcript_text, video_url, duration_seconds.
        Do NOT include any extra text, markdown, or code fences. Do NOT wrap the JSON in quotes or comments it should not be a string it should be JSON object.
    """
    ),
    response_model=YouTubeTranscript,
    show_tool_calls=True,
    use_json_mode=True,
)
