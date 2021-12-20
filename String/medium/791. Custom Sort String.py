class Solution:
    def customSortString(self, order: str, str: str) -> str:
        order_dict = {c : i for i,c in enumerate(order)}
        return "".join(sorted(str, key=lambda x : order_dict[x] if x in order_dict else 0))