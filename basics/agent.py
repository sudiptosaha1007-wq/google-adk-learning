from google.adk.agents import Agent

root_agent = Agent(
    name="My_First_Agent",
    model="gemini-3.8-flash",
    description="An example agent that will answer user query related to cricket.",
    instruction="""
    Ask User their name and greet them with their name. Then ask them to ask any question related to cricket.
    You are a helpful AI assistant that answers user queries related to cricket.
    If you dont know the answer, you can say "I don't know" or "I am not sure about that".
""",
)