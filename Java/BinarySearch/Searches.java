/* Author Norman Bernardi
   CIT-130
   3/23/22
   Binary Search Class Method
*/
package BinarySearch;
public class Searches 
{
   public static <T extends Comparable<T>> int bSearch(T[] arr, T key, int first, int last)
   {
    if(first > last)
        return -1;
    else
    {
        int middle = (first + last) / 2;
        int compResult = key.compareTo(arr[middle]);
        if(compResult == 0)
            return middle;
        else if (compResult < 0)
            return bSearch(arr, key, first, middle - 1);
        else
            return bSearch(arr, key, middle + 1, last);
    }
   }
   public static <T extends Comparable<T>> int binarySearch(T[] arr, T key){
      return bSearch(arr, key, 0, (arr.length - 1));
}
}

            
            

