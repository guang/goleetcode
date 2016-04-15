package main

import (
	"testing"
)

func TestAddSingleDigit(t *testing.T) {
	if result := addDigits(0); result != 0 {
		t.Errorf("Expected result of 0, but got %d instead.", result)
	}

	if result := addDigits(9); result != 9 {
		t.Errorf("Expected result of 9, but got %d instead.", result)
	}
}

func TestAddDoubleDigit(t *testing.T) {
	if result := addDigits(10); result != 1 {
		t.Errorf("Expected result of 1, but got %d instead.", result)
	}

	if result := addDigits(14); result != 5 {
		t.Errorf("Expected result of 5, but got %d instead.", result)
	}

	if result := addDigits(19); result != 1 {
		t.Errorf("Expected result of 1, but got %d instead.", result)
	}
}

func TestAddTripleDigit(t *testing.T) {
	if result := addDigits(100); result != 1 {
		t.Errorf("Expected result of 1, but got %d instead.", result)
	}

	if result := addDigits(123); result != 6 {
		t.Errorf("Expected result of 6, but got %d instead.", result)
	}

	if result := addDigits(987); result != 6 {
		t.Errorf("Expected result of 6, but got %d instead.", result)
	}
}
