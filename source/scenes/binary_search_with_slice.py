from manim import *
from input import arr, target

class BinarySearchWithSlice(Scene):
    def construct(self):
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
        self.play(*[Create(g[0]) for g in array_items], *[Write(g[1]) for g in array_items])
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
            "0. If array empty → return False",
            "1. Find middle element",
            "2. If middle == target → return True",
            "3a. If target < middle → search left",
            "3b. Else → search right"
        ]
        algo_texts = []
        for i, line in enumerate(algo_lines):
            t = Text(line, font_size=28, t2c={"→": WHITE}).to_edge(RIGHT).shift(UP * (1.5 - i * 0.7)).scale(0.8)
            algo_texts.append(t)
            self.add(t)

        def highlight_step(i):
            # Reset all to white
            for j, t in enumerate(algo_texts):
                t.set_color(WHITE)
            # Highlight current line
            algo_texts[i].set_color(YELLOW)
            self.wait(0.5)

        # ------------------------------
        # Binary search animation with algorithm highlighting
        # ------------------------------
        low = 0
        high = len(arr)

        # Initial pointer placement
        mid = (low + high) // 2
        low_label.next_to(array_items[low][0], DOWN)
        mid_label.next_to(array_items[mid][0], UP)
        high_label.next_to(array_items[high - 1][0], DOWN)

        while low < high:
            mid = (low + high) // 2

            # Step 0: check empty
            highlight_step(0)

            # Step 1: find middle
            highlight_step(1)
            self.play(mid_label.animate.next_to(array_items[mid][0], UP))

            # Step 2: check middle
            highlight_step(2)
            if arr[mid] == target:
                self.play(array_items[mid][0].animate.set_fill(GREEN, opacity=0.7))
                self.wait(1)
                break

            # Step 3a or 3b
            if arr[mid] > target:
                self.play(array_items[mid][0].animate.set_fill(ORANGE, opacity=0.7))
                self.wait(1)
                highlight_step(3)  # search left
                # discard right
                to_drop = VGroup(*array_items[mid:high])
                high = mid
            else:
                self.play(array_items[mid][0].animate.set_fill(ORANGE, opacity=0.7))
                self.wait(1)
                highlight_step(4)  # search right
                # discard left
                to_drop = VGroup(*array_items[low:mid+1])
                low = mid + 1

            # Animate discarded boxes dropping
            self.play(to_drop.animate.shift(DOWN * 2).set_opacity(0.5))

            # ------------------------------
            # Update pointers
            # ------------------------------
            # Offset L and R if pointing to the same box
            if low == high - 1:
                self.play(
                    low_label.animate.next_to(array_items[low][0], DOWN + LEFT * 0.3),
                    high_label.animate.next_to(array_items[low][0], DOWN + RIGHT * 0.3),
                )
            else:
                self.play(
                    low_label.animate.next_to(array_items[low][0], DOWN),
                    high_label.animate.next_to(array_items[high - 1][0], DOWN),
                )

            # Move mid pointer
            self.play(mid_label.animate.next_to(array_items[mid][0], UP))
            self.wait(0.5)
        self.wait(3)
