import asyncio
from google_adk import Agent, GraphWorkflow
from google_adk.models import GeminiModel

async def main():
    print("Initializing Google ADK Gemini Agent...")

    # Example initialization of a Gemini agent via ADK
    # This demonstrates the setup for a basic agent using the Gemini model.
    agent = Agent(
        name="GeminiHelper",
        description="A simple agent built using the Google ADK.",
        model=GeminiModel(model_name="gemini-1.5-pro")
    )

    # For ADK 2.0 graph workflow example
    workflow = GraphWorkflow(name="BasicInteraction")
    workflow.add_step("user_input", lambda req: req)
    workflow.add_step("agent_process", agent.run)
    workflow.connect("user_input", "agent_process")

    print("Agent is ready.")

    request = "Hello Gemini, can you explain the core concepts of Google ADK?"
    print(f"\nUser: {request}")

    try:
        # In a real environment with credentials, this would execute the graph
        # response = await workflow.execute(request)
        # print(f"Agent: {response}")
        print("Agent (Simulated Output): Google ADK brings classical programming structures to AI agents.")
    except Exception as e:
        print(f"Error running agent: {e}")

if __name__ == "__main__":
    asyncio.run(main())
