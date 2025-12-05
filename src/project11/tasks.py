from crewai import Task
from crewai_tools import SerperDevTool 

 
from dotenv import load_dotenv
load_dotenv()

search_tool = SerperDevTool()


class BookwriterTask:

    def Outline_Writer_Task(self,agent,topic):
        return Task(
            description= f"""Write a detailed outline for a book on the topic search on the
                    
                  internet for latest data of and trends on the topic and write a detailed outline for the book.
                  
                  
                 Parameters:
                    
                 -------------
                 topic:{topic}
            
                  """,
                    
            tools=[search_tool],
            agent=agent,
            expected_output= f"""A detailed outline for the book in the format of the following
            Topic:{topic}
            Outline:
            -Introduction
            -Chapter 1 with brief description
            -Chapter 2 with brief description
            -Chapter 3 with brief description
            -Chapter 4 with brief description
            -Chapter 5 with brief description
            -Conclusion
            -References """,

        )
    
    def Book_Writer_Task(self, agent, outline):
       return Task(
       description=f"""Write a book based on the outline and scraped data. The book should be well-structured and 
             written in a way that is easy to understand and follow.

       Parameters:
        -------------
       outline: {outline}
        """,
        agent=agent,  # Corrected this line
        expected_output="A complete well-formatted book with 200 pages and 5 chapters."
    )
    

    
