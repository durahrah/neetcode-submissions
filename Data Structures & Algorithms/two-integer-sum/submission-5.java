class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevmap = new HashMap<>();

        for(int i=0;i<nums.length;i++)
        {
            int num = nums[i];
            int diff = target - num;

            if(prevmap.containsKey(diff))
            {
                return new int[] {prevmap.get(diff), i};
            }
            prevmap.put(num,i);
        }
        return new int[] {};
    }
}
