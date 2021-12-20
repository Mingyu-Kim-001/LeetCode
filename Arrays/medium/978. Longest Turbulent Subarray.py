class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        first_case_len = second_case_len = 0
        cur_max = 0
        for i, num in enumerate(arr):
            if i == 0:
                prev = num
                continue
            if prev > num:
                if i % 2:
                    second_case_len += 1
                    cur_max = max(cur_max, first_case_len)
                    first_case_len = 0
                else:
                    first_case_len += 1
                    cur_max = max(cur_max, second_case_len)
                    second_case_len = 0
            elif prev < num:
                if i % 2 == 0:
                    second_case_len += 1
                    cur_max = max(cur_max, first_case_len)
                    first_case_len = 0
                else:
                    first_case_len += 1
                    cur_max = max(cur_max, second_case_len)
                    second_case_len = 0
            else:
                cur_max = max(cur_max, first_case_len, second_case_len)
                first_case_len = second_case_len = 0
            prev = num
        return max(cur_max, first_case_len, second_case_len) + 1