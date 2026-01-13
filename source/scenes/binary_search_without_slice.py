from manim import *
from input import arr, target

class BinarySearchWithoutSlice(Scene):
    """
    An animated visualization of binary search without slicing the array.

    This Manim scene demonstrates binary search on a given array `arr` to locate a 
    target value `target`, avoiding inefficient list slicing. Instead of removing elements,
    a green box highlights the current search space, and pointers L (low), M (middle),
    and R (high) are animated to indicate the search bounds.

    Features:
    - Displays a note at the beginning explaining why slicing is inefficient.
    - Shows the target value at the top.
    - Displays the array as a sequence of boxes with numbers.
    - Animates pointers for low (L), middle (M), and high (R) positions.
    - Highlights each step of the binary search algorithm on the right:
        0. If array empty -> return False
        1. Find middle element
        2. If middle == target -> return True
        3a. If target < middle -> search left
        3b. Else -> search right
    - Uses a green rectangle to indicate the current search space instead of dropping elements.
    - Updates pointers and offsets them visually if low and high coincide.
    - Highlights the middle element being considered in orange, and the target element in green
      once found.

    Attributes:
        arr (list): The array to perform binary search on, imported from `input.py`.
        target (int/float): The value to search for in `arr`, imported from `input.py`.

    Usage:
        python -m manim -pql binary_search_animation.py BinarySearchWithoutSlice
    """
    def construct(self):
         # ------------------------------
        # Justificatuion for not slicing
        # ------------------------------
        my_text = Text("Note that slicing creates new lists, which is inefficient.", font_size=32)
        self.play(Write(my_text))
        self.wait(2)
        self.play(FadeOut(my_text))

        # ------------------------------
        # Header showing target
        # ------------------------------
        header = Text(f"Binary Search (Target = {target})", font_size=32)
        header.to_edge(UP)
        self.play(Write(header))
        self.wait(1)

        # ------------------------------
        # Draw the full array shifted left
        # ------------------------------
        array_items = []
        for i, val in enumerate(arr):
            box = Square(side_length=1)
            box.shift(RIGHT * i)
            num = Text(str(val), font_size=36).move_to(box.get_center())
            group = VGroup(box, num)
            array_items.append(group)

        array_group = VGroup(*array_items).move_to(LEFT * 3)
        self.play(
            *[Create(g[0]) for g in array_items],
            *[Write(g[1]) for g in array_items]
        )
        self.wait(1)

        # ------------------------------
        # Pointers: L, M, R
        # ------------------------------
        low_label = Text("L", color=BLUE).scale(0.7)
        mid_label = Text("M", color=YELLOW).scale(0.7)
        high_label = Text("R", color=RED).scale(0.7)
        self.add(low_label, mid_label, high_label)

        # ------------------------------
        # Algorithm steps on the right
        # ------------------------------
        algo_lines = [
            "0. If array empty -> return False",
            "1. Find middle element",
            "2. If middle == target -> return True",
            "3a. If target < middle -> search left",
            "3b. Else -> search right"
        ]
        algo_texts = []
        for i, line in enumerate(algo_lines):
            t = Text(line, font_size=28, t2c={"->": WHITE}).to_edge(RIGHT).shift(UP * (1.5 - i * 0.7)).scale(0.8)
            algo_texts.append(t)
            self.add(t)

        def highlight_step(i):
            for j, t in enumerate(algo_texts):
                t.set_color(WHITE)
            algo_texts[i].set_color(YELLOW)
            self.wait(0.5)

        # ------------------------------
        # Binary search animation with green search space
        # ------------------------------
        low = 0
        high = len(arr) - 1

        # Initial pointer placement
        mid = (low + high) // 2
        low_label.next_to(array_items[low][0], DOWN)
        mid_label.next_to(array_items[mid][0], UP)
        high_label.next_to(array_items[high][0], DOWN)

        # Highlight box for search space
        search_space_box = SurroundingRectangle(VGroup(*array_items[low:high+1]), color=GREEN, buff=0.15)
        self.play(Create(search_space_box))
        self.wait(0.5)

        while low <= high:
            mid = (low + high) // 2

            # Step 0
            highlight_step(0)
            # Step 1
            highlight_step(1)
            self.play(mid_label.animate.next_to(array_items[mid][0], UP))

            # Step 2
            highlight_step(2)
            if arr[mid] == target:
                self.play(array_items[mid][0].animate.set_fill(GREEN, opacity=0.7))
                self.wait(1)
                break

            # Step 3a or 3b
            if arr[mid] > target:
                self.play(array_items[mid][0].animate.set_fill(ORANGE, opacity=0.7))
                self.wait(1)
                highlight_step(3)
                high = mid - 1
            else:
                self.play(array_items[mid][0].animate.set_fill(ORANGE, opacity=0.7))
                self.wait(1)
                highlight_step(4)
                low = mid + 1

            # Update search space rectangle
            new_rect = SurroundingRectangle(VGroup(*array_items[low:high+1]), color=GREEN, buff=0.15)
            self.play(Transform(search_space_box, new_rect))

            # Update pointers
            if low <= high:
                if low == high:
                    # Offset L and R if pointing to same box
                    self.play(
                        low_label.animate.next_to(array_items[low][0], DOWN + LEFT * 0.3),
                        high_label.animate.next_to(array_items[low][0], DOWN + RIGHT * 0.3),
                    )
                else:
                    self.play(
                        low_label.animate.next_to(array_items[low][0], DOWN),
                        high_label.animate.next_to(array_items[high][0], DOWN),
                    )
                self.play(mid_label.animate.next_to(array_items[mid][0], UP))

            self.wait(0.5)

        self.wait(3)
