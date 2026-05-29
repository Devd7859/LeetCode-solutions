class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Ensure A is the smaller array to optimize binary search time complexity to O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Index for A
            j = half - i - 2  # Index for B
            
            # Boundary conditions handling
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2:
                    return min(Aright, Bright)
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                
            elif Aleft > Bright:
                r = i - 1  # Too many elements from A's left side, move left
            else:
                l = i + 1  # Too few elements from A's left side, move right