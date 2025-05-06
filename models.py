from typing import List, Optional
from pydantic import BaseModel, Field


class YouTubeTranscript(BaseModel):
    """Model for YouTube transcript data"""
    video_id: str
    video_title: str
    transcript_text: str
    video_url: str
    duration_seconds: Optional[int] = None


class BlogPost(BaseModel):
    """Model for blog post content"""
    title: str = Field(..., description="SEO-optimized title for the blog post")
    meta_description: str = Field(..., description="SEO meta description for the blog post, 150-160 characters")
    keywords: List[str] = Field(..., description="List of SEO keywords relevant to the blog post")
    content: str = Field(..., description="Full HTML/Markdown content of the blog post")
    word_count: int = Field(..., description="Total word count of the blog post")
    headings: List[str] = Field(..., description="List of all headings in the blog post")


class BlogAnalysis(BaseModel):
    """Model for blog quality analysis"""
    quality_score: int = Field(..., description="Overall quality score from 1-100")
    seo_score: int = Field(..., description="SEO optimization score from 1-100")
    readability_score: int = Field(..., description="Readability score from 1-100")
    strengths: List[str] = Field(..., description="List of strengths of the blog post")
    weaknesses: List[str] = Field(..., description="List of areas for improvement")
    improvement_suggestions: List[str] = Field(..., description="Specific suggestions for improvement")
    is_publishable: bool = Field(..., description="Whether the blog post meets publishing standards")


class FinalBlog(BaseModel):
    """Model for the final improved blog with markdown"""
    blog_post: BlogPost
    analysis: BlogAnalysis
    markdown: str = Field(..., description="Final markdown representation of the blog post") 