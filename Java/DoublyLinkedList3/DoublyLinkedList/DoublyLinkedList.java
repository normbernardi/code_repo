package DoublyLinkedList;
public class DoublyLinkedList<T>
{
    private class Node<T>
    {
        private T data;
        private Node<T> next;
        private Node<T> prev;

        public Node( )
        {
             data = null;
             next = null;
             prev = null;
        }

        public Node(T newData, Node<T> nextValue, Node<T> prevValue)
        {
            data = newData;
            next = nextValue;
            prev = prevValue;
        }
     }//End of Node<T> inner class

   private Node<T> head = null;
   private Node<T> tail = null;
   public class DoublyLinkedIterator
   {
    // We do not need a previous node when using a doubly linked list
      private Node<T> position = null;

      public DoublyLinkedIterator( )
      {
         position = head;
      }
      public Node<T> getPosition()
      {
         return position;
      }
         
      public void restart( )
      {
         position = head;
      }
      public T next( )
      {
         if (!hasNext( ))
            throw new IllegalStateException( );
         T toReturn = position.data;
         position = position.next;
         return toReturn;
      } // end of next()

      public void insertHere(T newData)
      {
         if (position == null && head != null)
         {
            // Add to end. First move a temp
            // pointer to the end of the list
            Node<T> temp = head;
            while (temp.next != null)
            temp = temp.next;
            temp.next = new Node<T>(newData, temp, null);
            }
         else if (head == null || position.prev == null)
            // at head of list
            DoublyLinkedList.this.addToStart (newData);
         else
         {
            // Insert before the current position
            Node<T> temp = new Node<T>(newData,
            position.prev, position);
            position.prev.next = temp;
            position.prev = temp;
         }
      } // end of insertHere()
      public void delete( )
   {
      if (position == null)
         throw new IllegalStateException( );
      else if (position.prev == null)
      { // Deleting first node
         head = head.next;
         position = head;
      }
      else if (position.next == null)
      { // Deleting last node
         position.prev.next = null;
         position = null;
      }
      else
      {
         position.prev.next = position.next;
         position.next.prev = position.prev;
         position = position.next;
      }
   } // end of delete()
   
   public boolean hasNext()
   {
      if (position != null)
      {
         return true;
      }
      else
      {
         tail = position;
         return false;
      }
   } // end of hasNext()
   
   public T peek()
   {
      if (!hasNext())
         throw new IllegalStateException();
      return position.data;
   } // end of peek()
} // DoublyLinkedIterator
    
      public DoublyLinkedIterator iterator( )
      {
         return new DoublyLinkedIterator( );
      }
      public DoublyLinkedList( )
      {
         head = null;
      }
          
      public DoublyLinkedList(DoublyLinkedList list)
      {
         this.head = list.head;
      }
   
       /**
        Adds a node at the start of the list with the specified data.
        The added node will be the first node in the list.
       */
      public void addToStart(T itemData)
      {
         head = new Node<T>(itemData, head, null);
      }
       /**
        Removes the head node and returns true if the list contains at least
        one node. Returns false if the list is empty.
       */
       public boolean deleteHeadNode( )
       {
           if (head != null)
           {
               head = head.prev;
               return true;
           }
           else
               return false;
       }
   
       /**
        Returns the number of nodes in the list.
       */
       public int size( )
       {
           int count = 0;
           Node<T> position = head;
           while (position != null)
           {
               count++;
               position = position.next;
           }
           return count;
       }
   
       public boolean contains(T item)
       {
           return (find(item) != null);
       }
   
       /**
        Finds the first node containing the target item, and returns a
        reference to that node. If target is not in the list, null is returned.
       */
       private Node<T> find(T target)
       {
           Node<T> position = head;
           T itemAtPosition;
           while (position != null)
           {
               itemAtPosition = position.data;
               if (itemAtPosition.equals(target))
                   return position;
               position = position.next;
           }
           return null; //target was not found
       }
   
       /**
        Finds the first node containing the target and returns a reference
         to the data in that node. If target is not in the list, null is returned.
       */
       public T findData(T target)
       {
           return find(target).data;
       }
   
       public String toString( )
       {
         String output = "";
         DoublyLinkedList.DoublyLinkedIterator j = this.iterator();
         Node<T> position = head;
         while (j.hasNext())
            output += (j.next() + "\n");
         return output;
       }
   
       public boolean isEmpty( )
       {
           return (head == null);
       }
   
       public void clear( )
       {
           head = null;
       }
   
      /*
       For two lists to be equal they must contain the same data items in
       the same order. The equals method of T is used to compare data items.
      */
      public boolean equals(Object otherObject)
       {
           if (otherObject == null)
               return false;
           else if (getClass( ) != otherObject.getClass( ))
               return false;
           else
           {
               DoublyLinkedList<T> otherList = (DoublyLinkedList<T>)otherObject;
               if (size( ) != otherList.size( ))
                   return false;
               Node<T> position = head;
               Node<T> otherPosition = otherList.head;
               while (position != null)
               {
                   if (!(position.data.equals(otherPosition.data)))
                       return false;
                   position = position.next;
                   otherPosition = otherPosition.next;
               }
               return true; //no mismatch was not found
           }
       }
      public void outputBackwards() {
         String[] list = this.toString().split("\n");
         for(int i = list.length-1; i >= 0; i--)
            System.out.println(list[i] + ""); 
      }
      public DoublyLinkedList clone(DoublyLinkedIterator i)
      {
      DoublyLinkedList newList = new DoublyLinkedList();
      DoublyLinkedList.DoublyLinkedIterator j = newList.iterator();
      newList.head = this.head;
      while (i.hasNext())
      {
         j.insertHere(i.peek());
      }
      return newList;
   }
}