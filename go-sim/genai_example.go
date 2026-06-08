package main

import (
	"context"
	"fmt"
	"log"

	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	// Initialize the GenAI client. It will automatically pick up
	// the GEMINI_API_KEY environment variable.
	client, err := genai.NewClient(ctx, nil)
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	// Using the gemini-2.0-flash model for best performance and cost
	result, err := client.Models.GenerateContent(
		ctx,
		"gemini-2.0-flash",
		genai.Text("Explain how AI works in a few words"),
		nil,
	)
	if err != nil {
		log.Fatalf("Failed to generate content: %v", err)
	}

	// Output the resulting text from the model
	if result != nil {
		text := result.Text()
		fmt.Println(text)
	} else {
		fmt.Println("No result generated.")
	}
}
