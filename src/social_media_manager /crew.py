from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List

@CrewBase
class SocialMediaManager():
    """SocialMediaManager crew – Personalized outreach to BJJ/MMA athletes"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_manager'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # type: ignore[index]
        )

    @task
    def dm_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['dm_generation_task'],  # type: ignore[index]
            output_file='generated_dm.txt'  # Changed from report.md
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SocialMediaManager crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,  # Use integer for more detailed logs (CrewAI supports this in recent versions)
            # memory=True,  # optional
            # planning=True,  # optional
        )
