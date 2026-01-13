from manim import *
from scenes.binary_search_with_slice import BinarySearchWithSlice
from scenes.binary_search_without_slice import BinarySearchWithoutSlice

arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

scene1 = BinarySearchWithSlice()
scene2 = BinarySearchWithoutSlice()
scene1.render()
scene2.render()


