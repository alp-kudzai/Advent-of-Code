package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Create a new reader to read from standard input
	f, err := os.Open("sample.txt")
	if err != nil {
		panic(err)
	}
	reader := bufio.NewReader(f)
	defer f.Close()

	// Keep track of the sum of the priorities of the item types that appear in both compartments
	var sum int

	// Read each line from standard input
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}

		// Remove leading and trailing whitespace from the line
		line = strings.TrimSpace(line)

		// Split the line into two compartments
		compartments := strings.SplitN(line, "", len(line)/2)

		// Check if any item type appears in both compartments
		for _, c := range compartments[0] {
			if strings.ContainsRune(compartments[1], c) {
				// If an item type appears in both compartments, calculate its priority and add it to the sum
				priority := int(c-'a') + 1
				if c >= 'A' && c <= 'Z' {
					priority += 26
				}
				sum += priority
				break
			}
		}
	}

	// Print
	fmt.Printf("\nTotal: %v", sum)
}
