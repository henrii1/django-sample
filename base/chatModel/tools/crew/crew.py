import os

from crewai import Crew, Process
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from .agent import CourseContentAgent
from .task import CourseContentTask

from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY_TWO")

def course_content_crew(course_query, current_level, desired_level):
    """Generates personalized course contents based on user's specifications"""
    agents = CourseContentAgent
    tasks = CourseContentTask

    google_agent = agents.google_search_agent
    bing_agent = agents.bing_search_agent
    compile_agent = agents.compile_agent

    google_task = tasks.google_task(
        agent=google_agent,
        course_query=course_query,
        current_level=current_level,
        desired_level=desired_level
    )

    bing_task = tasks.bing_task(
        agent=bing_agent,
        course_query=course_query,
        current_level=current_level,
        desired_level=desired_level
    )

    compile_task = tasks.combine_task(
        agent=compile_agent,
        course_query=course_query,
        current_level=current_level,
        desired_level=desired_level,
        context=[google_task, bing_task]
    )

    crew = Crew(
        agents=[google_agent, bing_agent, compile_agent],
        tasks = [google_task, bing_task, compile_task],
        process = Process.hierarchical,
        manager_llm = ChatOpenAI(api_key = openai_api_key, model='gpt-4', temperature=0)
    )

    result = crew.kickoff()
    return result
