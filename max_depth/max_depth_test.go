package main

import (
	"testing"
)

func TestEmptyTree(t *testing.T) {
	root := deserialize("[]")
	printTree(root)

	if result := maxDepth(root); result != 1 {
		t.Errorf("Expected result of 1, but got %d instead.", result)
	}
}

func TestOneLevel(t *testing.T) {
	root := deserialize("[0]")
	printTree(root)

	if result := maxDepth(root); result != 1 {
		t.Errorf("Expected result of 1, but got %d instead.", result)
	}
}

func TestTwoLevelsComplete(t *testing.T) {
	root := deserialize("[0,1,2]")
	printTree(root)

	if result := maxDepth(root); result != 2 {
		t.Errorf("Expected result of 2, but got %d instead.", result)
	}
}

func TestThreeLevelsComplete(t *testing.T) {
	root := deserialize("[0,1,2,3,4,5,6]")
	printTree(root)

	if result := maxDepth(root); result != 3 {
		t.Errorf("Expected result of 3, but got %d instead.", result)
	}
}

func TestLeft(t *testing.T) {
	root := deserialize("[0,1,nil,2,nil,3]")
	printTree(root)

	if result := maxDepth(root); result != 4 {
		t.Errorf("Expected result of 4, but got %d instead.", result)
	}
}

func TestRight(t *testing.T) {
	root := deserialize("[0,nil,1,nil,2,nil,3]")
	printTree(root)

	if result := maxDepth(root); result != 4 {
		t.Errorf("Expected result of 4, but got %d instead.", result)
	}
}

func TestZigZag(t *testing.T) {
	root := deserialize("[0,nil,1,2,nil,nil,3]")
	printTree(root)

	if result := maxDepth(root); result != 4 {
		t.Errorf("Expected result of 4, but got %d instead.", result)
	}
}
