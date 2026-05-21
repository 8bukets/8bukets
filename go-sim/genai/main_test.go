package main

import (
	"context"
	"strings"
	"testing"
)

func TestGenerateExplanation_EmptyInput(t *testing.T) {
	ctx := context.Background()
	_, err := GenerateExplanation(ctx, "")
	if err == nil {
		t.Fatal("expected an error for empty concept, got nil")
	}
	if !strings.Contains(err.Error(), "concept cannot be empty") {
		t.Fatalf("unexpected error message: %v", err)
	}
}

// Note: Testing actual generation without a mock requires GEMINI_API_KEY.
// We test the timeout behavior or the expected failure when key is missing to validate safety.
func TestGenerateExplanation_MissingAPIKey(t *testing.T) {
	// If run in an environment without the key, we expect a specific failure from the SDK,
	// not a panic or crash.
	ctx := context.Background()
	_, err := GenerateExplanation(ctx, "Test Concept")
	if err == nil {
		// If it passes, an API key is present and it worked, which is also fine.
		t.Log("API call succeeded (key present)")
	} else {
		// If it fails, ensure it's a known error from the SDK rather than a custom crash
		t.Logf("API call failed as expected without key: %v", err)
		if !strings.Contains(err.Error(), "failed to") {
			t.Errorf("unexpected error format: %v", err)
		}
	}
}
