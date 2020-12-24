import java.util.*;

class LinkedList implements Iterable
{

	private class Node
	{
		private Object data;
		private Node next;

		Node(Object input)
		{
			data = input;
			next = null;
		}
	}

	private Node head;
	private int count;

	public void display()
	{
		for(Node current = head; current != null; current = current.next)
		{
			System.out.printf("%s\n", current.data);
		}
	}

	public void insertFirst(Object data)
	{
		Node newNode = new Node(data);
		newNode.next = head;
		head = newNode;
		count++;
	}

	public void insertLast(Object data)
	{

		if(count == 0)
		{
			insertFirst(data);
		}
		else
		{
			Node newNode = new Node(data);

			Node current = head;
			while(current.next != null)
			{
				current = current.next;
			}

			current.next = newNode;
			count++;
		}
	}

	public boolean isEmpty()
	{
		if(head == null)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	public Object peekFirst()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else
		{
			return head.data;
		}
	}

	public Object peekLast()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else
		{
			Node current = head;
			while(current.next != null)
			{
				current = current.next;
			}
			return current.data;
		}
	}

	public Object removeFirst()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else
		{
			Node firstNode = head;
			head = firstNode.next;
			count--;
			return firstNode.data;
		}

	}

	public Object removeLast()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else if(count == 1)
		{
			Object onlyValue = removeFirst();
			count--;
			return onlyValue;
		}
		else
		{
			Node current = head;
			Node previousNode = null;
			while(current.next != null)
			{
				previousNode = current;
				current = current.next;
			}
			Node lastNode = current;
			previousNode.next = null;
			count--;
			return lastNode.data;
		}
	}

	public int count()
	{
			return count;
	}

	public Iterator iterator()
	{
		return  new myLinkedListIterator(this);
	}

	private class myLinkedListIterator implements Iterator
	{
		private Node iterNext;
		public myLinkedListIterator(LinkedList theList)
		{
			iterNext = theList.head;
		}

		public boolean hasNext()
		{
			return (iterNext != null);
		}

		public Object next()
		{
			Object value;
			if(iterNext == null)
			{
				value = null;
			}
			else
			{
				value = iterNext.data;
				iterNext = iterNext.next;
			}
			return value;
		}
		public void remove()
		{
			throw new UnsupportedOperationException("Not supported");
		}
	}

}
