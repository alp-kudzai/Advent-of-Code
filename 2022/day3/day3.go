package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"runtime"
	"strings"
)

var Elves []string
var FILENAME = "input.txt"
var POINTS = make(map[string]int)
var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

//fill in the score

func fillPoint() {
	for n, l := range chars {
		l_str := string(l)
		POINTS[l_str] = n + 1
	}
}

func handleErr(err error) {
	if err != nil {
		_, filename, line, _ := runtime.Caller(1)
		log.Printf("[error] %s:%d %v", filename, line, err)
		panic(err)
	}
}

func getData() []string {
	//returns a nested slice with each backpack as its own slice
	//[[elfbag]]
	var elves []string
	f, err := os.Open(FILENAME)
	handleErr(err)
	fCont := bufio.NewScanner(f)
	for fCont.Scan() {
		bag := fCont.Text()
		elves = append(elves, bag)
	}
	return elves
}

func contains(sl []string, str string) bool {
	var ans = false
	for _, s := range sl {
		if s == str {
			ans = true
			break
		}
	}
	return ans
}

func processElf(bag string) string {
	//we process an elf's bag
	// we split the string in half
	// i always compare the 1stHalf vs. 2ndHalf
	//if the item im comparing is in the other half return that item(letter)
	// if item is not in there then store it so you dont search for it again
	str_half := (len(bag) / 2) - 1
	half1, half2 := bag[:str_half+1], bag[str_half+1:]
	//log.Printf("\n1st: %v\n2nd: %v\nLen: %v", half1, half2, str_half)
	var memo []string
	var result string
	var stop = false
	for i := 0; i < str_half+1; i++ {
		chStr := string(half1[i])
		//log.Println(chStr)
		for oi := 0; oi < str_half+1; oi++ {
			otStr := string(half2[oi])
			if otStr == chStr {
				result = otStr
				stop = true
				break
			}
			check := contains(memo, chStr)
			if check == false {
				memo = append(memo, chStr)
				//log.Println(memo)
			}
		}
		if stop {
			break
		}
	}
	return result
}

// part2
func getGroups(elves []string) [][]string {
	//given the elves bags, we return the elves in groups of 3
	//E.G elves[[g1,g1,g1], [g2,g2,g2]]
	var group []string
	var groups [][]string
	for _, bag := range elves {
		group = append(group, bag)
		if len(group) == 3 {
			groups = append(groups, group)
			group = nil
		}
	}
	return groups
}

func getCommon(el1 string, el2 string, el3 string) string {
	var memo []string
	var common string
	for _, i := range el1 {
		i_str := string(i)
		if contains(memo, i_str) {
			continue
		} else if strings.Contains(el2, i_str) {
			if strings.Contains(el3, i_str) {
				common = i_str
			}
		} else {
			memo = append(memo, i_str)
		}
	}
	return common
}

func findBadge(group []string) string {
	var Badge string
	el1, el2, el3 := group[0], group[1], group[2]
	common1 := getCommon(el1, el2, el3)
	if common1 != "" {
		Badge = common1
	} else {
		log.Fatalf("Didnt get expected result: %v", common1)
	}

	return Badge
}

func processGroups(elves []string) int {
	var Total int
	elfGroups := getGroups(elves)
	var badges []string
	for _, group := range elfGroups {
		Badge := findBadge(group)
		score := POINTS[Badge]
		badges = append(badges, Badge)
		Total += score
	}
	fmt.Printf("\nBadges:\n%v\nTotal: %v", badges, Total)
	return Total
}

func main() {
	fillPoint()
	// fmt.Println(POINTS)
	Elves = getData()
	// var Total int
	// for _, bag := range Elves {
	// 	l := processElf(bag)
	// 	point := POINTS[l]
	// 	Total += point
	// }
	// fmt.Printf("The Sum: %v\n", Total)
	priority_points := processGroups(Elves)
	fmt.Printf("\n\nTotal Priority Points: %v\n", priority_points)
}

//RULES
//Each bag has 2 compartments
//Items in bag are divided evenly into those compartments
//find the common item in both compartments, thats the mistake made by the elf
//items are letters a-z A-Z
//items have priorities a-z 1-26 & A-Z 27-52

//Part2 Rules
//Badge is item carried by all 3 elves
//3 elves make a group
//find the elves badges
