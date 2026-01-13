# Binary Search Animation (Manim)

This project demonstrates **Binary Search** using [Manim](https://www.manim.community/) with visual pointers, array halving, dropping discarded elements, and step-by-step algorithm highlighting. Designed for CS1010A.

---

## Features

- Visual representation of the array  
- L (Left), M (Middle), and R (Right) pointers  
- Array halving with discarded elements dropping visually  
- Algorithm steps displayed on the right, highlighted as executed  
- Target element clearly indicated  

---

## Installation

Make sure you have Python 3 installed. Then, install Manim:

```bash
pip install manim
```

Change the arr and target for the binary search by replacing the default arguments in input.py
```python
arr = [1,3,5,7,9,11,13]
target = 9
```

## Running the Animation
Open a terminal and navigate to the folder containing the animation:

```bash
cd source
```

Generate each animation with Manim:
You may select the quality of the video by changing -pqh with -pql

High Quality
```bash
python -m manim -pqh binary_search_animation.py BinarySearchWithoutSlice
python -m manim -pqh binary_search_animation.py BinarySearchWithSlice
```

Low Quality
```bash
python -m manim -pql binary_search_animation.py BinarySearchWithoutSlice
python -m manim -pql binary_search_animation.py BinarySearchWithSlice
```

Stitch the videos by first updating the videos_to_concat.txt

For High Quality
```txt
file 'media/videos/binary_search_animation/1080p60/BinarySearchWithSlice.mp4'
file 'media/videos/binary_search_animation/1080p60/BinarySearchWithoutSlice.mp4'
```

For Low Quality
```txt
file 'media/videos/binary_search_animation/480p15/BinarySearchWithSlice.mp4'
file 'media/videos/binary_search_animation/480p15/BinarySearchWithoutSlice.mp4'
```

Then, run the following command on bash:

For High Quality
```bash
ffmpeg -f concat -safe 0 -i videos_to_concat.txt -c copy media/videos/binary_search_animation/1080p60/CombinedBinarySearch.mp4
```

For Low Quality
```bash
ffmpeg -f concat -safe 0 -i videos_to_concat.txt -c copy media/videos/binary_search_animation/480p15/CombinedBinarySearch.mp4
```

## Output video 
Output video will be saved automatically as CombinedBinarySearch.mp4 in the folder

For High Quality
```swift
media/videos/binary_search_animation/1080p60/
```

For Low Quality
```swift
media/videos/binary_search_animation/480p15/
```