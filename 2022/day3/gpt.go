package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Open the file for reading
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Create a scanner to read the file
	scanner := bufio.NewScanner(file)

	// Keep a running total of the sum of the intersection characters
	var sum int

	// Loop over each line in the file
	for scanner.Scan() {
		line := scanner.Text()

		// Split the line in half
		halfLen := len(line) / 2
		firstHalf := line[:halfLen]
		secondHalf := line[halfLen:]

		// Find the intersection characters shared by both halves
		// and add them to the sum
		for _, c := range firstHalf {
			if strings.ContainsRune(secondHalf, c) {
				// Calculate the numeric value of the character
				// according to the given key (a-z=1-26, A-Z=27-52)
				var val int
				if c >= 'a' && c <= 'z' {
					val = int(c-'a') + 1
				} else if c >= 'A' && c <= 'Z' {
					val = int(c-'A') + 27
				}

				// Add the character's value to the sum
				sum += val
			}
		}
	}

	// Print the final sum
	fmt.Println(sum)
}
