package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"
	"time"

	"google.golang.org/genai"
)

// GenerateExplanation calls the Gemini API to explain a given concept.
// It includes timeouts and input validation for security and resilience.
func GenerateExplanation(ctx context.Context, concept string) (string, error) {
	if concept == "" {
		return "", errors.New("concept cannot be empty")
	}

	// Set a 15-second timeout to prevent hanging calls
	ctx, cancel := context.WithTimeout(ctx, 15*time.Second)
	defer cancel()

	client, err := genai.NewClient(ctx, nil)
	if err != nil {
		return "", fmt.Errorf("failed to create client: %w", err)
	}

	prompt := fmt.Sprintf("Explain how %s works in a few words", concept)

	// Use gemini-2.0-flash for optimal cost and performance
	result, err := client.Models.GenerateContent(
		ctx,
		"gemini-2.0-flash",
		genai.Text(prompt),
		nil,
	)
	if err != nil {
		return "", fmt.Errorf("failed to generate content: %w", err)
	}

	if result != nil {
		text := result.Text()
		if text == "" {
			return "", errors.New("received empty response from model")
		}
		return text, nil
	}

	return "", errors.New("no result generated")
}

func main() {
	// Validate environment configuration securely without logging secrets
	if os.Getenv("GEMINI_API_KEY") == "" {
		log.Println("WARNING: GEMINI_API_KEY is not set. The GenAI API call will likely fail unless using a mock/proxy.")
	}

	ctx := context.Background()
	fmt.Println("Requesting explanation for AI...")

	explanation, err := GenerateExplanation(ctx, "AI")
	if err != nil {
		log.Fatalf("Execution Error: %v", err)
	}

	fmt.Println("Result:", explanation)
}
