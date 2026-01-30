class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {

            // Convert string to char array
            char[] arr = s.toCharArray();

            // Sort the characters
            Arrays.sort(arr);

            // Convert back to string (key)
            String key = new String(arr);

            // If key not present, create new list
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }

            // Add original string to the list
            map.get(key).add(s);
        }

        // Return all grouped values
        return new ArrayList<>(map.values());
    }
}
