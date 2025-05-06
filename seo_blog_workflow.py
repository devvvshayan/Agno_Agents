# d:\Agno-Agents\seo_blog_workflow.py

from agno.workflow import Workflow
from transcript_agent import transcript_agent
from blog_writer_agent import blog_writer_agent
from blog_analyzer_agent import blog_analyzer_agent
from blog_refiner_agent import blog_refiner_agent
from langtrace_python_sdk import langtrace
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())


langtrace.init()


class SEOBlogWorkflow(Workflow):
    """
    Simple SEO blog workflow:
      1. Fetch transcript
      2. Write blog post
      3. Analyze blog
      4. Refine if needed
    """

    def run_workflow(self, youtube_url: str):  
        # 1. Fetch transcript  
        transcript_response = transcript_agent.run(youtube_url)  
        transcript = transcript_response.content  # Extract content from RunResponse  
        
        print("transcript done " )
        # 2. Generate blog post  
        blog_response = blog_writer_agent.run(transcript.transcript_text)  
        blog = blog_response.content  # Extract content from RunResponse  
        
        print("blog done " )
        # 3. Analyze quality  
        analysis_response = blog_analyzer_agent.run(blog.content)  
        analysis = analysis_response.content  # Extract content from RunResponse  
        
        print("analysis done " )
        # 4. Refine if not publishable  
        if not analysis.is_publishable:
            print("Refining blog post...")  
            refined_response = blog_refiner_agent.run(  
                {"blog_post": blog, "analysis": analysis}  
            )  
            blog = refined_response.content.blog_post  
        
        return blog


if __name__ == "__main__":
    # Example usage
    youtube_url = "https://www.youtube.com/watch?v=lLJbHHeFSsE"
    # Instantiate workflow
    workflow = SEOBlogWorkflow()
    # Run the workflow with the YouTube URL
    result = workflow.run_workflow(youtube_url)
    print(result)
