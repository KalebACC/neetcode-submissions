class Solution {
    public boolean isValid(String s) {
        String openingChar = "({[";
        String closingChar = ")}]";
        Stack<Character> closing = new Stack<>();

        for (char value : s.toCharArray())
        {
            //Opening character
            if (openingChar.indexOf(value) != -1)
            {
                closing.push(closingChar.charAt(openingChar.indexOf(value)));
            }

            //closing Character
            else if(closingChar.indexOf(value) != -1)
            {
                if (closing.isEmpty()) return false;

                if (closing.pop() != value) return false;
            }
            else
            {
                return false;
            }
        }
        if (closing.isEmpty()) return true;
        return false;
    }
}
