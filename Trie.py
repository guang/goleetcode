#!/bin/python

class Node(object):
  
  def __init__(self):
    self.children = {}
    self.is_leaf = False

class Trie(object):

  def __init__(self):
    self.root = Node()

  def insert(self, val):
    current = self.root
    for char in val:
      if char in current.children:
        current = current.children[char]
      else:
        current.children[char] = Node()
        current = current.children[char]
    current.is_leaf = True

  def search(self, word):
    if len(self.root.children) < 1:
      return False
    current = self.root
    for char in word:
      if char not in current.children:
        return False
      else:
        current = current.children[char]
    return current.is_leaf

  def prefix(self, prefix):
    if len(self.root.children) < 1:
      return False
    current = self.root
    for char in prefix:
      if char not in current.children:
        return False
      else:
        current = current.children[char]
    return True

  def autocomplete(self, prefix):
    if len(self.root.children) < 1:
      return []
    current = self.root
    for char in prefix:
      if char not in current.children:
        return []
      else:
        current = current.children[char]
    return set(self.find_words(current, prefix, []))

  def find_words(self, node, prefix, word_list):
    for char in node.children:
      if len(node.children[char].children) < 1 and node.children[char].is_leaf == True:
        return word_list.append(prefix+char)
      elif  node.children[char].is_leaf == True:
        word_list.append(prefix+char)
        self.find_words(node.children[char], prefix+char, word_list)
      else:
        self.find_words(node.children[char], prefix+char, word_list)
    return word_list

  def print_root(self):
    print(self.root.children)

if __name__ == "__main__":
  trie = Trie()
  trie.insert("ronak")
  trie.insert("ronnie")
  trie.insert("ron")
  trie.insert("ronaknnathani")
  trie.insert("ronni")
  print(trie.search("ronak"))
  words = trie.autocomplete("ron")
  print(words)
