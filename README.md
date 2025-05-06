# SEO Blog Writer System

A multi-agent system that generates high-quality, SEO-optimized blog posts from YouTube video transcripts.

## Features

- **YouTube Transcript Fetching**: Extracts and processes transcripts from YouTube videos
- **SEO Blog Writing**: Creates well-structured, engaging, and SEO-optimized blog posts
- **Content Quality Analysis**: Evaluates blog post quality across multiple dimensions
- **Content Refinement**: Improves content based on analysis feedback
- **Markdown Generation**: Produces clean, publication-ready markdown

## System Architecture

The system uses a multi-agent workflow with specialized agents:

1. **Transcript Agent**: Fetches and processes YouTube video transcripts
2. **Blog Writer Agent**: Creates SEO-optimized blog posts from transcripts
3. **Blog Analyzer Agent**: Evaluates blog quality and provides feedback
4. **Blog Refiner Agent**: Improves content based on analysis feedback

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your Google API key for Gemini:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   MODEL_ID=gemini-1.5-pro
   ```

## Usage

Run the workflow with:

```
python seo_blog_workflow.py
```

You'll be prompted to:
1. Enter a YouTube video URL
2. Specify a minimum quality score threshold (default: 80)

The system will:
1. Fetch and process the video transcript
2. Generate a blog post
3. Analyze quality
4. Refine if needed
5. Save the final markdown to `generated_blog.md`

## Requirements

- Python 3.8+
- Google API key for Gemini
- Required Python packages (see requirements.txt)

## License

MIT
