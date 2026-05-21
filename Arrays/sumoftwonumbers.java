import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            
            int complement = target - nums[i];

            if(map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }

            map.put(nums[i], i);
        }

        return new int[] {};
    }

    public static void main(String[] args) {
        // Create an instance of the Solution class
        Solution solution = new Solution();

        // Define a test case
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        // Call the method and capture the result
        int[] result = solution.twoSum(nums, target);

        // Print the result using Arrays.toString() so it's readable
        System.out.println("Resulting indices: " + Arrays.toString(result));
    }
} 