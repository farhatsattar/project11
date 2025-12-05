from .agents import MyBookWriterAgents
from .tasks import BookwriterTask
from crewai import Crew  # type: ignore

def writer(data):
    agents = MyBookWriterAgents()
    tasks = BookwriterTask()

    Book_Writer = agents.Book_Writer()
    Book_Writer_Task = tasks.Book_Writer_Task(
        agent=Book_Writer,
        outline=data
    )

    crew = Crew(
        tasks=[Book_Writer_Task],
        agents=[Book_Writer],
        verbose=True,
    )

    result = crew.kickoff()
    print(result)
    return result  # Return the result for further use


