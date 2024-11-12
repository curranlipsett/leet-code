using System;
using two_sum;
namespace two_sum;

class Program
{

    // Main Method
    static void Main(String[] args)
    {
        TwoSum newSolution = new TwoSum();
        int[] result = newSolution.CalculateSum(new int[] { 1, 2, 3, 4, 5, 6, 7, 8 }, 14);

        foreach (int i in result)
        {
            Console.WriteLine(i);
        }
    }
}