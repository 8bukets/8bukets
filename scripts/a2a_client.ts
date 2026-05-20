async function main() {
  const SERVER_URL = 'http://localhost:8080';

  console.log("=== Multi-Agent Workflow Demonstration ===");
  console.log("Main Agent: I need help from a specialist. Let me check its capabilities.");

  try {
    // 1. Discover the agent's capabilities
    const cardResponse = await fetch(`${SERVER_URL}/.well-known/agent-card`);
    if (!cardResponse.ok) {
        throw new Error(`Failed to fetch agent card: ${cardResponse.statusText}`);
    }
    const agentCard = await cardResponse.json();
    console.log("\nMain Agent: Found specialist agent card:");
    console.log(`- Name: ${agentCard.name}`);
    console.log(`- Description: ${agentCard.description}`);
    console.log(`- Transport: ${agentCard.preferredTransport}`);
    console.log(`- Invoke URL: ${agentCard.url}`);

    console.log("\nMain Agent: I will now delegate a task to the specialist.");

    // 2. Invoke the agent via JSON-RPC
    const rpcRequest = {
      jsonrpc: "2.0",
      id: "req-workflow-1",
      method: "message/send",
      params: {
        message: {
          role: "user",
          parts: [
            {
              kind: "text",
              text: "What is 2+2?"
            }
          ]
        }
      }
    };

    console.log("\nMain Agent: Sending request ->", JSON.stringify(rpcRequest.params.message.parts[0].text));

    const invokeResponse = await fetch(agentCard.url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(rpcRequest)
    });

    if (!invokeResponse.ok) {
        throw new Error(`Failed to invoke agent: ${invokeResponse.statusText}`);
    }

    const rpcResult = await invokeResponse.json();

    // 3. Process the result
    if (rpcResult.error) {
        console.error("\nSpecialist Agent Error:", rpcResult.error);
    } else {
        const responseText = rpcResult.result.artifacts[0].parts[0].text;
        console.log("\nSpecialist Agent responded ->", responseText);
        console.log("\nMain Agent: Workflow completed successfully.");
    }

  } catch (error) {
    console.error("Workflow failed:", error);
  }
}

main();