from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import PDFSearchTool, SerperDevTool

@CrewBase
class BuckleConsultCrewAutomationRecommendationCrew():
    """BuckleConsultCrewAutomationRecommendation crew"""

    @agent
    def DiscoveryAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['DiscoveryAgent'],
            tools=[ScrapeWebsiteTool(), PDFSearchTool(), SerperDevTool()],
        )

    @agent
    def AnalysisAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['AnalysisAgent'],
            tools=[PDFSearchTool(), SerperDevTool(), ScrapeWebsiteTool()],
        )

    @agent
    def RecommendationAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['RecommendationAgent'],
            tools=[PDFSearchTool("solutions.pdf"), SerperDevTool(), ScrapeWebsiteTool()],
        )


    @task
    def discovery_task(self) -> Task:
        return Task(
            config=self.tasks_config['discovery_task'],
            tools=[PDFSearchTool("solutions.pdf"), SerperDevTool(), ScrapeWebsiteTool()],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            tools=[PDFSearchTool("solutions.pdf"), SerperDevTool(), ScrapeWebsiteTool()],
        )

    @task
    def recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommendation_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the BuckleConsultCrewAutomationRecommendation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            memory_config={
            "provider": "mem0",
            "config": {"user_id": "crew_user_1"},
        }
        )
