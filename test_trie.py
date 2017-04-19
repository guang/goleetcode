#!/bin/python

import pytest
from Trie import Trie

testdata = [
    ("ronak", True),
    ("ronnie", True),
    ("ronni", True),
    ("austin", True),
    ("alyssa", True),
    ("zubair", True),
    ("kelly", False)]

@pytest.fixture(scope="session")
def trie():
  trie = Trie()
  yield trie

@pytest.fixture(scope="session")
def insert(trie):
  trie.insert("ronak")
  trie.insert("ronnie")
  trie.insert("austin")
  trie.insert("alyssa")
  trie.insert("ronni")
  trie.insert("zubair")

@pytest.mark.parametrize("word, expected", testdata)
def test_search(insert, trie, word, expected):
  assert trie.search(word) == expected


testdata_prefix = [
    ("r", True),
    ("ron", True),
    ("alyssa", True),
    ("zub", True),
    ("emi", False)]

@pytest.mark.parametrize("prefix, expected", testdata_prefix)
def test_prefix(insert, trie, prefix, expected):
  assert trie.prefix(prefix) == expected


testdata_autocomplete = [
    ("r", {"ronak", "ronni", "ronnie"}),
    ("ronn", {"ronni", "ronnie"}),
    ("a", {"alyssa", "austin"}),
    ("al", {"alyssa"})]

@pytest.mark.parametrize("prefix, expected", testdata_autocomplete)
def test_autocomplete(insert, trie, prefix, expected):
  assert trie.autocomplete(prefix) == expected
