package main

import (
	"testing"
)

func TestDummy(t *testing.T) {
	root := deserialize("[0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,nil,5]")
	printTree(root)
	/*
		if result := maxDepth(root); result != 1 {
			t.Errorf("Expected result of 1, but got %d instead.", result)
		}
	*/
}
