package main

import (
	"fmt"
	"strconv"
	"strings"
)

func reverse(x int) int {
    
	intString := strconv.Itoa(x)

	if x < 0 {
		// If negative, remove the minus sign and add later
		intString = strings.Replace(intString, "-", "", -1)
	}
	var returnSlice string

	for i := len(intString)-1; i >= 0; i-- {
		
		if intString[i] != 0 {
		    returnSlice += string(intString[i])
		}
	}

	var returnInt, err = strconv.Atoi(returnSlice)

	if err != nil {
		fmt.Print(err)
	}

	if x < 0 {
		returnInt *= -1
	}

	if returnInt > 2147483648 || returnInt < -2147483648 {
		return 0
	}
	
	return int(returnInt)
	
}

func main() {
	fmt.Println(reverse(1534236469))
}