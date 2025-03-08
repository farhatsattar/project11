from .agents import MyBookWriterAgents
from .tasks import BookwriterTask
from crewai import Crew

Topic = "Artificial intelligence in 2025"




agents = MyBookWriterAgents()
tasks = BookwriterTask()

#agent1
Outline_writer = agents.Outline_Writer()


#agent2
Book_Writer = agents.Book_Writer()

#task1
Outline_writer_Task = tasks.Outline_Writer_Task(
    agent= Outline_writer,
    topic= Topic
)

#Task2
Book_Writing_Task =  tasks.Book_Writer_Task(
         agent= Book_Writer,
         outline = [Outline_writer_Task]
    
)



crew = Crew(
    tasks = [Outline_writer_Task,Book_Writing_Task],
    agents = [Outline_writer,Book_Writer],
    verbose = True,
)


      
  
def Last():
    results = crew.kickoff()
    print(results)
    