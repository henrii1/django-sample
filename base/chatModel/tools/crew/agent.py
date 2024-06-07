import os

from crewai import Agent
from langchain_community.chat_models import ChatOllama
from langchain_openai.chat_models import ChatOpenAI

from tools.crew.tools.google_scrapper import GoogleScrapeTool
from tools.crew.tools.bing_scrapper import BingScrapeTool
from tools.crew.tools.rag_tool import RagTool
from tools.crew.tools.search_tool import SearchTools

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY_TWO")

class CourseContentAgent:

    def __init__(self):
        self.ollama = ChatOllama(model="llama3")  #try a variant of llama3
        self.openai = ChatOpenAI(api_key=api_key, model='gpt-3.5-turbo', temperature=0)

    def google_search_agent(self):
        return Agent(
            role= """Expert at analysing course data scrapped from google, a RAG system as
            well as you training data to arrive at the most comprehensive course outline for the
            given user query specifying a particular course the user intents to learn.""",
            goal = """compare the information available to you from various sources as well as your 
                    internal training data to develop the most optimal course content possible.                                        
            """,
            backstory='An expert in analyzing the course data and compiling the best informations for creating the most comprehensive course based on the user query',
            tools = [
                GoogleScrapeTool.google_scrape,
                RagTool.rag_tool
            ],
            verbose=False,
            allow_delegation=False,
            llm=self.openai
        )
    
    def bing_search_agent(self):
        return Agent(
            role= """Expert at analysing course data scrapped from microsoft bing, a RAG system as
            well as you training data to arrive at the most comprehensive course outline for the
            given user query specifying a particular course the user intents to learn.""",
            goal = """compare the information available to you from various sources as well as your 
                    internal training data to develop the most optimal course content possible.
            """,
            backstory='An expert in analyzing the course data and compiling the best informations for creating the most comprehensive course based on the user query',
            tools= [
                BingScrapeTool.bing_scrape,
                RagTool.rag_tool
            ],
            verbose=False,
            allow_delegation=False,
            llm=self.openai
        )
    
    def compile_agent(self):
        return Agent(
            role = "Expert in analysing the course generation output from two agents, and outputing the best result by combining relevant parts from both",
            goal = """compare the information available to you from various sources as well as your 
                    internal training data to develop the most optimal course content possible.
            """,
            backstory='An expert in analyzing the course data and compiling the best informations for creating the most comprehensive course based on the user query',
            tools = [
                SearchTools.search_internet,
            ],
            llm = self.openai

        )