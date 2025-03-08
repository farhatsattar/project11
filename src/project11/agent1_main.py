
from .agents import MyBookWriterAgents
from .tasks import BookwriterTask
from crewai import Crew


def outline_writer(topic):
    agents = MyBookWriterAgents()
    tasks = BookwriterTask()

    Outline_Writer = agents.Outline_Writer()
    Outline_Writer_Task = tasks.Outline_Writer_Task(
        agent=Outline_Writer,
        topic=topic
    )

    Outline_Crew = Crew(
        tasks=[Outline_Writer_Task],
        agents=[Outline_Writer],
        verbose=True,
    )

    results = Outline_Crew.kickoff()
    return results  # Returning results for further use