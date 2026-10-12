class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        num_per = math.factorial(len(nums))
        arr = nums.copy()
        seen = {tuple(arr)}
        res = [arr.copy()]

        while len(res) < num_per:
            random.shuffle(arr)
            t = tuple(arr)
            if t not in seen:
                seen.add(t)
                res.append(arr.copy())

        return res