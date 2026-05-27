/**
 * Automates the creation of a Run Task in HCP Terraform
 */

async function createRunTask() {
  const tfeToken = process.env.TFE_TOKEN;
  if (!tfeToken) {
    console.error("Error: TFE_TOKEN environment variable is not set.");
    process.exit(1);
  }

  const organizationId = process.env.HCP_ORGANIZATION_ID || "626eb9aa-6f12-40a0-af3c-0b8fc325049e";
  const url = `https://app.terraform.io/api/v2/organizations/${organizationId}/tasks`;

  const hmacKey = process.env.HMAC_KEY;
  if (!hmacKey) {
    console.error("Error: HMAC_KEY environment variable is not set.");
    process.exit(1);
  }

  const payload = {
    data: {
      type: "tasks",
      attributes: {
        name: "packer-validation",
        url: "https://api.cloud.hashicorp.com/packer/2023-01-01/terraform-cloud/validation/f638d299-57d6-4ea4-96c5-d936811c468f",
        "hmac-key": hmacKey,
        description: "Packer validation run task for HCP Terraform",
        category: "task",
        enabled: true
      }
    }
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${tfeToken}`,
        'Content-Type': 'application/vnd.api+json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`Failed to create Run Task. Status: ${response.status} ${response.statusText}`);
      console.error(`Response: ${errorText}`);
      process.exit(1);
    }

    const responseData = await response.json();
    console.log("Successfully created Run Task:", responseData.data.id);
  } catch (error) {
    console.error("Error executing API request:", error);
    process.exit(1);
  }
}

// IIFE to run the async function
(async () => {
  await createRunTask();
})().catch(console.error);
