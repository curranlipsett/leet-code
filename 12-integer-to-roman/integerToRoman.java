import java.util.*;

class integerToRoman {  
    public String intToRoman(int num) {
        StringBuilder returnString = new StringBuilder();
        HashMap<Integer, String> vals = new LinkedHashMap<Integer,String>();

        vals.put(1000, "M");
        vals.put(900, "CM");
        vals.put(500, "D");
        vals.put(400, "CD");
        vals.put(100, "C");
        vals.put(90, "XC");
        vals.put(50, "L");
        vals.put(40, "XL");
        vals.put(10, "X");
        vals.put(9, "IX");
        vals.put(5, "V");
        vals.put(4, "IV");
        vals.put(1, "I");

        while (num > 0) {
            // Iterate through the vals list to find the largest number that will go into our remainder

            for (Integer val : vals.keySet()) {
                if (num >= val) {
                    num = num - val;
                    returnString.append(vals.get(val));
                    break;
                }
            }
        }
        return returnString.toString();
    }

    public static void main(String args[]) {
        integerToRoman newSol = new integerToRoman();
        System.out.println(newSol.intToRoman(0));
    }
}
