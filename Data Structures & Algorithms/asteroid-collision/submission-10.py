class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < -asteroid:
                    stack.pop()              # Top asteroid explodes
                elif stack[-1] == -asteroid:
                    stack.pop()              # Both explode
                    alive = False
                else:
                    alive = False            # Current asteroid explodes

            if alive:
                stack.append(asteroid)

        return stack