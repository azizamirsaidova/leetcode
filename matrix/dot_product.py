"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVectorand vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.


"""
from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))

    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0

        i = 0
        j = 0

        # while j is less than the length of orginal nums 
        # and j is less than vector nums
        while j < len(self.nums) and j < len(vec.nums):
            # access the indexes, and values of nums and vector
            i_idx, i_num = self.nums[i]
            j_idx, j_num = vec.nums[j]

            if i_idx == j_idx:
                dot_product = (i_num * j_num)
                i += 1
                j += 1
            elif i_idx > j_idx:
                j += 1
            else:
                i += 1
        return dot_product

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print(v1.dotProduct(v2))