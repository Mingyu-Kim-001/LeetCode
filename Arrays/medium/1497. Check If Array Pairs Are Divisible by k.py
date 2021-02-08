class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k==1: return True
        residuals_count = [0]*k
        sum_residuals_count = 0
        for i in arr:
            residual = i%k
            comp_residual = k-residual if residual!=0 else 0
            if residuals_count[comp_residual]>0:
                residuals_count[comp_residual]-=1
                # sum_residuals_count-=1
            else:
                residuals_count[residual]+=1
                # sum_residuals_count+=1
            
        return sum(residuals_count)==0