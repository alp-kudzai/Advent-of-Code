package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var FILENAME = "input.txt"

func handleErr(err error, funcName string) {
	if err != nil {
		log.Fatalf("%v\nIn Func: %v", err, funcName)
	}
}

func parseFile() [][]int {
	//used to parse the file according to the rules
	//
	var Elves [][]int
	var single []int // a single elve
	f, err := os.Open(FILENAME)
	handleErr(err, "parseFile")

	file_contents := bufio.NewScanner(f)

	for file_contents.Scan() {
		if file_contents.Text() != "" {
			str_cal := file_contents.Text()
			calorie, err := strconv.Atoi(str_cal)
			handleErr(err, "parseFile_Loop")
			single = append(single, calorie)
		} else {
			Elves = append(Elves, single)
			single = nil
		}
	}

	Elves = append(Elves, single)
	defer f.Close()
	return Elves
}

func trackCalories(elves [][]int) []int {
	//given a slice of elves, we will determine who has the most calories on them
	// return a slice with [index, total]
	//intially slice is [0,0]
	tracker := make([]int, 2)
	for i, el := range elves {
		//here we loop over single elves
		//each elf has one more calorie in a slice
		total := 0
		for _, cal := range el {
			//looping over the calories in an elf's bag
			total += cal
		}
		if total > tracker[1] {
			tracker[0], tracker[1] = i, total
		}
	}
	return tracker
}

func RemoveIndex(s [][]int, index int) [][]int {
	return append(s[:index][:], s[index+1:][:]...)
}

func sumSlices(el [][]int) int {
	total := 0
	for _, v := range el {
		total += v[1]
	}
	return total
}
func main() {
	Elves := parseFile()
	var elvesMost [][]int
	for i := 0; i < 3; i++ {
		elf := trackCalories(Elves)
		elvesMost = append(elvesMost, elf)
		Elves = RemoveIndex(Elves, elf[0])
	}
	Total := sumSlices(elvesMost)
	//log.Printf(elvesMost) //uncomment to see part1
	fmt.Printf("The top 3 elves are carrying: %d calories!", Total)
	//find the elve with the most amount of calories
}
