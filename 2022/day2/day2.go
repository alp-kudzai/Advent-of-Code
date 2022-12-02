package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var FILENAME = "input.txt"

// 1st column is the Opponent, 2nd column is Me
// A,X => Rock
// B,Y => Paper
// C,Z => scissors
// Total score => sum of rounds
// Round => shape + outcome
// Shape: Rock 1, Paper 2, Scissors 3
// Outcome: Lost 0, Draw 3, Win 6
var (
	A, X    = "Rock", "Rock"
	B, Y    = "Paper", "Paper"
	C, Z    = "Scissors", "Scissors"
	R, P, S = 1, 2, 3 //scores for shape
	L, D, W = 0, 3, 6 //Lost, Draw, Win

)

func compScore(res, shape int) int {
	//compute score given result and shape
	var score = res + shape
	return score
}

func logic(opp, me string) int {
	//brain. Given two shapes, we determine wins, loses or draws
	var score int
	switch opp {
	case "A":
		//Rock
		if me == "Y" {
			//if im paper then i win else i lose or draw
			score = compScore(W, P)
			// log.Print(score)
		} else if me == "X" {
			score = compScore(D, R)
		} else {
			score = compScore(L, S)
		}
	case "B":
		//Paper
		if me == "Z" {
			//win, scissors
			score = compScore(W, S)
		} else if me == "Y" {
			//draw, Paper
			score = compScore(D, P)
		} else {
			//lose, Rock
			score = compScore(L, R)
		}
	case "C":
		//Scissors
		if me == "X" {
			//win, Rock
			score = compScore(W, R)
		} else if me == "Z" {
			//Draw, Scissors
			score = compScore(D, S)
		} else {
			//lose, Paper
			score = compScore(L, P)
		}
	default:
		fmt.Println(opp, me)
	}
	// log.Print(score)
	return score
}

func play(moves [][]string) int {
	//loop over moves
	// Opp => moves[][0]
	// Me => moves[][1]
	var Total = 0
	for _, shps := range moves {
		opp, me := shps[0], shps[1]
		score := logic(opp, me)
		// log.Print(score)
		Total += score
	}
	return Total
}

func handleErr(err error, funcName string) {
	if err != nil {
		log.Fatalf("%v\nIn Func: %v", err, funcName)
	}
}

func getFile() [][]string {
	//Parse the file and return a slice with slices
	//[[Opp,Me]]
	var container [][]string
	f, err := os.Open(FILENAME)
	handleErr(err, "getFile")
	contents := bufio.NewScanner(f)
	for contents.Scan() {
		line := contents.Text()
		line_arr := strings.Split(line, " ")
		container = append(container, line_arr)
	}
	return container
}

// PART2
// X => Lose
// Y => Draw
// Z => Win
func decide(opp, req string) []int {
	//given what the Opp played
	//and the requirements
	//return shape
	var outcome []int
	switch opp {
	case "A":
		//Rock
		if req == "X" { //Lose
			outcome = append(outcome, L, S)
		} else if req == "Y" {
			//Draw
			outcome = append(outcome, D, R)
		} else {
			//Win
			outcome = append(outcome, W, P)
		}
	case "B":
		//Paper
		if req == "X" { //Lose
			outcome = append(outcome, L, R)
		} else if req == "Y" {
			//Draw
			outcome = append(outcome, D, P)
		} else {
			//Win
			outcome = append(outcome, W, S)
		}
	case "C":
		//Scissors
		if req == "X" { //Lose
			outcome = append(outcome, L, P)
		} else if req == "Y" {
			//Draw
			outcome = append(outcome, D, S)
		} else {
			//Win
			outcome = append(outcome, W, R)
		}
	}
	return outcome
}
func logic2(opp, req string) int {
	var score int
	outcome := decide(opp, req)
	score = compScore(outcome[0], outcome[1])
	return score
}

func play2(games [][]string) int {
	//play the games
	// loop over the games
	// opp => games[][0]
	// requirements => games[][1]
	//return Total
	var Total int
	for _, g := range games {
		opp, req := g[0], g[1]
		res := logic2(opp, req)
		Total += res
	}
	return Total
}

func main() {
	games := getFile()
	Total := play(games)
	Total2 := play2(games)
	fmt.Printf("\nPart 1 Total Score: %v\n", Total) //PART 1
	fmt.Printf("\nPart 2 Total Score: %v\n", Total2)
}
