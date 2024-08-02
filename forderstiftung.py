import os
from crewai import Crew, Process
from crewai import Task
from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool
search_tool = SerperDevTool()

#enter the website of a foundation website that contains deatils about grant making criteria
ws_tool = WebsiteSearchTool(website='https://www.stiftung-mercator.de/de/wie-wir-foerdern/informationen-fuer-antragstellende/foerderkriterien/')

# Creating a senior researcher agent with memory and verbose mode
leadership = Agent(
  role='Board of Directors',
  goal='Creates decision based on Funding Rules of foundation if project is funded or not',
  verbose=True,
  memory=True,
  backstory=(
    "Supporting the strategic framework is the Board of Directors, which governs the foundation "
    "by establishing policies and making critical decisions, crucial for "
    "maintaining adherence to the foundation's mission and values."
  ),
  tools=[search_tool,ws_tool],
  allow_delegation=True
)

# Creating a writer agent with custom tools and delegation capability
management = Agent(
  role='Program Officer',
  goal='managing grant making programs, from reviewing applications to monitoring grantee performance',
  verbose=True,
  memory=True,
  backstory=(
    "The Program Officer plays a vital role in managing grant making programs, from reviewing applications to "
    "monitoring grantee performance, ensuring that funds are used effectively to meet the foundation’s goals."
  ),
  tools=[search_tool,ws_tool],
  allow_delegation=True
)

# Creating a writer agent with custom tools and delegation capability
operations = Agent(
  role='Operational Efficiency and Community Engagement',
  goal='enhances operational efficiency',
  verbose=True,
  memory=True,
  backstory=(
    'The Grants Manager enhances operational efficiency by overseeing the administrative aspects of grants, '
    'including compliance and fund disbursement, ensuring that the processes align with policies. The '
    'Development/Fundraising Manager is key in securing funds, organizing fundraising events, and managing donor '
    'relations, essential for the foundation\'s sustainability and growth.'
  ),
  tools=[search_tool],
  allow_delegation=False
)



# Board task
leadership_task = Task(
  description=(
    "You are the Board and ultimate deciders"
    "You get pre filtered grant requests with a recommendation from management"
    "You decide if the Project aligns with the foundation"
    "its market opportunities, and potential risks."

  ),
  expected_output='a decision if the projects is funded or not, along with a explanation ',
  tools=[search_tool,ws_tool],
  agent=leadership
)

# Organizing task
management_task = Task(
  description=(
    "You are the management team of the foundation"
    "You make sure funded projects align with the foundation"
    "You make sure the leadership/board gets standard documents about projects so they can decide about funding"
    "You add a recommendation"
    "Check the website to check details about the decision making process"
  ),
  expected_output='A comprehensive analysis for the leadership board about the project. this includes the most '
                  'important project details, details on how exactly the project aligns with the foundation goals on '
                  'the website and a comprehensive recommendation.',
  tools=[search_tool,ws_tool],
  agent=management,
  output_file='board_meeting.md'  # Example of output customization
)

# Create Grantrequest
grantrequest = Task(
  description=(
    "Create a exemplary project grant request for a project owner"
    "The project has to do with animals"
    "The grant request needs to contain everything a exemplary grant request needs to contain."
  ),
  expected_output='GrantRequest that will be used to decide if the project will be funded or not',
  tools=[search_tool],
  agent=operations,
  async_execution=False,
)

# Inform Projectowner
operations_OUT_task = Task(
  description=(
    "Compose an insightful answer email to the requesting organisation"
    "Focus on the decision process and explain the process"
    "This email should be easy to understand, engaging, and positive."
  ),
  expected_output='A mail to the requesting organisation with the decision',
  tools=[search_tool],
  agent=operations,
  async_execution=False,
  output_file='answer.md'  # Example of output customization
)



# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[leadership, management, operations],
  tasks=[grantrequest, management_task,leadership_task,operations_OUT_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True,
  embedder={
    "provider": "huggingface",
    "config": {
      "model": "mixedbread-ai/mxbai-embed-large-v1",  # https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
    }
  }
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff()
print(result)