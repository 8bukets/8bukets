import { Agent, GraphWorkflow } from '@google/adk';
import { GeminiModel } from '@google/adk/models';

async function main() {
  console.log("Initializing Google ADK Gemini Agent...");

  // Example initialization of a Gemini agent via ADK in TypeScript
  const agent = new Agent({
    name: "GeminiHelper",
    description: "A simple agent built using the Google ADK.",
    model: new GeminiModel({ modelName: "gemini-1.5-pro" })
  });

  // For ADK 2.0 graph workflow example
  const workflow = new GraphWorkflow({ name: "BasicInteraction" });
  workflow.addStep("user_input", (req) => req);
  workflow.addStep("agent_process", async (input) => await agent.run(input));
  workflow.connect("user_input", "agent_process");

  console.log("Agent is ready.");

  const request = "Hello Gemini, can you explain the core concepts of Google ADK?";
  console.log(`\nUser: ${request}`);

  try {
    // In a real environment with credentials, this would execute the graph
    // const response = await workflow.execute(request);
    // console.log(`Agent: ${response}`);
    console.log("Agent (Simulated Output): Google ADK brings classical programming structures to AI agents.");
  } catch (error) {
    console.error(`Error running agent: ${error}`);
  }
}

main().catch(console.error);
