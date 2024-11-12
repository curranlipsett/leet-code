package main

import (
	"fmt"
	"slices"
)
func main() {
    var arr1 = []int {1,2}
	var arr2 = []int {3,4}

	fmt.Printf("%f\n", findMedianSortedArrays(arr1, arr2))
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
		combined := append(nums1, nums2...)
		slices.Sort(combined)
		arrLen := len(combined)
		midPoint := arrLen / 2

		if  arrLen % 2 == 0 {
			var median = float64((combined[midPoint] + combined[midPoint - 1])) / 2.0
			return float64(median)
		}

		fmt.Print("combined: ", combined)
		fmt.Print("arrLen: ", arrLen)
		
		return float64(combined[midPoint])
}