package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// Task represents a unit of work in the system
type Task struct {
	ID          int
	Description string
	Completed   bool
}

// Agent represents a role in the Antigravity system
type Agent struct {
	Name string
	Role string
}

// simulateWork mimics an agent doing work over time
func (a *Agent) processTasks(tasks <-chan Task, results chan<- Task, wg *sync.WaitGroup) {
	defer wg.Done()
	for task := range tasks {
		fmt.Printf("[%s:%s] Started working on task %d: %s\n", a.Role, a.Name, task.ID, task.Description)

		// Simulate processing time
		time.Sleep(time.Duration(rand.Intn(1000)+500) * time.Millisecond)

		task.Completed = true
		fmt.Printf("[%s:%s] Finished task %d\n", a.Role, a.Name, task.ID)

		// Send completed task to results channel
		results <- task
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	fmt.Println("🚀 Starting 8bukets Parallel Simulation...")
	fmt.Println("=========================================")

	// Define agents based on the Antigravity ecosystem
	agents := []Agent{
		{Name: "Alpha", Role: "Chief AI Officer"},
		{Name: "Beta", Role: "Coder"},
		{Name: "Gamma", Role: "Reviewer"},
		{Name: "Delta", Role: "Cloud Workflow"},
	}

	// Channels for tasks
	numTasks := 10
	tasksCh := make(chan Task, numTasks)
	resultsCh := make(chan Task, numTasks)

	var wg sync.WaitGroup

	// Start agent workers in parallel
	for i := range agents {
		wg.Add(1)
		go agents[i].processTasks(tasksCh, resultsCh, &wg)
	}

	// Create and enqueue tasks (Work Orders)
	for i := 1; i <= numTasks; i++ {
		tasksCh <- Task{
			ID:          i,
			Description: fmt.Sprintf("Autonomous Work Order #%d", i),
		}
	}
	close(tasksCh) // No more tasks will be added

	// Wait for all workers to finish in a separate goroutine
	// so we can close the results channel
	go func() {
		wg.Wait()
		close(resultsCh)
	}()

	// Collect results
	completedCount := 0
	for task := range resultsCh {
		if task.Completed {
			completedCount++
		}
	}

	fmt.Println("=========================================")
	fmt.Printf("✅ Simulation Complete. Successfully processed %d/%d tasks.\n", completedCount, numTasks)
}
