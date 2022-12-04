package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"runtime"
	"strconv"
	"strings"
)

var FILENAME = "input.txt"

// create an elf struct with ranges
type Elf struct {
	from, to int
}

func intersection(s1, s2 []int) (inter []int) {
	hash := make(map[int]bool)
	for _, e := range s1 {
		hash[e] = true
	}
	for _, e := range s2 {
		// If elements present in the hashmap then append intersection list.
		if hash[e] {
			inter = append(inter, e)
		}
	}
	//Remove dups from slice.
	inter = removeDups(inter)
	return
}

// Remove dups from slice.
func removeDups(elements []int) (nodups []int) {
	encountered := make(map[int]bool)
	for _, element := range elements {
		if !encountered[element] {
			nodups = append(nodups, element)
			encountered[element] = true
		}
	}
	return
}

// Inspired by: https://stackoverflow.com/questions/44956031/how-to-get-intersection-of-two-slice-in-golang
func fullInter(el1, el2 []int) bool {
	answer := true
	hash := make(map[int]bool)
	if len(el1) >= len(el2) {
		for _, e := range el1 {
			hash[e] = true
		}
		for _, e := range el2 {
			if !hash[e] {
				answer = false
				break
			}
		}
	} else {
		for _, e := range el2 {
			hash[e] = true
		}
		for _, e := range el1 {
			if !hash[e] {
				answer = false
				break
			}
		}
	}
	return answer
}

func (e Elf) getRange() []int {
	//returns the range which the elf will be cleaning
	var rng []int
	for id := e.from; id < e.to+1; id++ {
		rng = append(rng, id)
	}
	return rng
}

func handleErr(err error) {
	if err != nil {
		_, filename, line, _ := runtime.Caller(1)
		log.Printf("[error] %s:%d %v", filename, line, err)
		panic(err)
	}
}

func toInt(str string) int {
	intStr, err := strconv.Atoi(str)
	handleErr(err)
	return intStr
}

func processData(str string) []Elf {
	//process the data
	// return a slice with the elf pair
	// str => 2-4,6-8
	elves := strings.Split(str, ",")    //["2-4","6-8"]
	el1 := strings.Split(elves[0], "-") //["2","4"]
	el2 := strings.Split(elves[1], "-")
	elf1 := Elf{from: toInt(el1[0]), to: toInt(el1[1])}
	elf2 := Elf{from: toInt(el2[0]), to: toInt(el2[1])}
	return []Elf{elf1, elf2}

}

func getData() [][]Elf {
	data, err := os.Open(FILENAME)
	defer data.Close()
	handleErr(err)
	content := bufio.NewScanner(data)
	var Elves [][]Elf
	for content.Scan() {
		line := content.Text()
		elfPair := processData(line)
		Elves = append(Elves, elfPair)
	}
	return Elves

}

func getOverlap(pair []Elf) bool {
	elf1, elf2 := pair[0], pair[1]
	overlap := fullInter(elf1.getRange(), elf2.getRange())
	return overlap
}

func getOverlap2(pair []Elf) []int {
	elf1, elf2 := pair[0], pair[1]
	overlap := intersection(elf1.getRange(), elf2.getRange())
	return overlap
}

func processOverlaps2(elves [][]Elf) map[string]any {
	var counter int
	var inters [][]int
	container := make(map[string]any)
	for _, pair := range elves {
		result := getOverlap2(pair)
		if len(result) > 0 {
			counter += 1
			inters = append(inters, result)
		}
	}
	container["number"] = counter
	container["intersections"] = inters
	return container
}

func processOverlaps(elves [][]Elf) (counter int) {
	// loop over elves and getOverlap
	// check len, if len 0 then there is no overlap
	for _, pair := range elves {
		result := getOverlap(pair)
		if result {
			counter += 1
		}
	}
	return
}
func main() {
	Elves := getData()
	result := processOverlaps(Elves)
	result2 := processOverlaps2(Elves)
	fmt.Printf("\nPart 1\nThe number of complete overlaps: %v\n\n", result)
	fmt.Printf("Part 2\nThe number of intersections: %v\n", result2["number"])
}
