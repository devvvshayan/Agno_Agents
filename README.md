# SEO Blog Writer System

A multi-agent system that generates high-quality, SEO-optimized blog posts from YouTube video transcripts using Agno and Gemini.

## Features

- **YouTube Transcript Fetching**: Extracts and processes transcripts from YouTube videos
- **SEO Blog Writing**: Creates well-structured, engaging, and SEO-optimized blog posts
- **Content Quality Analysis**: Evaluates blog post quality across multiple dimensions
- **Content Refinement**: Improves content based on analysis feedback
- **Markdown Generation**: Produces clean, publication-ready markdown

## System Architecture

The system uses a multi-agent workflow with specialized agents built on the Agno framework:

1. **Transcript Agent**: Fetches and processes YouTube video transcripts using built-in YouTubeTools
2. **Blog Writer Agent**: Creates SEO-optimized blog posts from transcripts
3. **Blog Analyzer Agent**: Evaluates blog quality and provides feedback
4. **Blog Refiner Agent**: Improves content based on analysis feedback

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   uv venv
   ```
3. Install dependencies:
   ```
   uv sync
   ```
4. Create a `.env` file with your Google API key for Gemini:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

Run the workflow with:

```
uv run seo_blog_workflow.py
```

The workflow will:
1. Fetch and process the video transcript from the specified YouTube URL
2. Generate an SEO-optimized blog post
3. Analyze the blog's quality
4. Refine the content if it doesn't meet publishing standards
5. Return the final blog post

You can modify the example YouTube URL in the script or update the workflow to accept user input as needed.

## Requirements

- Python 3.13+
- Google API key for Gemini
- Required Python packages:
  - agno >= 1.4.3
  - duckduckgo-search >= 8.0.1
  - google-genai >= 1.13.0
  - langtrace-python-sdk >= 3.8.17
  - python-dotenv >= 1.1.0
  - youtube-transcript-api >= 1.0.3
  - And other dependencies listed in pyproject.toml

## Model Information

The system uses Gemini models for AI capabilities:
- Default model: gemini-2.5-flash-preview-04-17

## License

MIT
