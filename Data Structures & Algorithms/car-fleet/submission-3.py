class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carpos = [(p,s) for p,s in zip(position,speed)]

        carpos.sort(reverse=True)

        stack = []
        stack.append((target-carpos[0][0])/carpos[0][1])

        for pos, spe in carpos:
            time = (target - pos) / spe
            if time > stack[-1]:
                stack.append(time)

        return len(stack)