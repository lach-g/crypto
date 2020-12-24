public class LinkedList
{

	private class Node
	{
		private Object data;
		private Node next;
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
		Node newNode = new Node();
		newNode.data = data;
		newNode.next = head;
		head = newNode;
		count++;
	}

	public void insertLast(Object data)
	{
		Node newNode = new Node();
		newNode.data = data;

		Node current = head;
		while(current.next != null)
		{
			current = current.next;
		}

		current.next = newNode;
		newNode.next = null;
		count++;
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
			Node lastNode = removeFirst();
		}
		else
		{
			Node previousNode;
			Node current = head;
			while(current.next != null)
			{
				previousNode = current;
				current = current.next;
			}
			Node lastNode = current;
			previousNode.next = null;
		}
		return lastNode;

	}


}
