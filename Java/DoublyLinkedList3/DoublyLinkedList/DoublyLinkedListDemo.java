package DoublyLinkedList;
public class DoublyLinkedListDemo
{
   public static void main(String[] args)
   {
      DoublyLinkedList list = new DoublyLinkedList();
      DoublyLinkedList.DoublyLinkedIterator i = list.iterator();
      list.addToStart("shoes");
      list.addToStart("orange juice");
      list.addToStart("coat");
      System.out.println("List contains: ");
      System.out.println(list.toString());
      System.out.println("List backwards:");
      list.outputBackwards();
      System.out.println(" ");
      System.out.println("List copy constructor");
      DoublyLinkedList list2 = new DoublyLinkedList(list);
      DoublyLinkedList.DoublyLinkedIterator j = list2.iterator();
      System.out.println("List 2 contains:");
      System.out.println(list2.toString());
      System.out.println("List clone");
      DoublyLinkedList list3 = list.clone(i);
      DoublyLinkedList.DoublyLinkedIterator k = list3.iterator();
      System.out.println("List 3 contains:");
         while (k.hasNext())
            System.out.println(k.next());
   }
}
      