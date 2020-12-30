import java.util.*;

class LinkedList<T> implements Iterable
{

	private class Node<T>
	{
		private T data;
		private Node<T> next;

		Node(T data)
		{
			this.data = data;
			this.next = null;
		}
	}

	private Node<T> head;
	private int count = 0;

	public void display()
	{
		for(Node<T> current = head; current != null; current = current.next)
		{
			System.out.printf("%s\n", current.data);
		}
	}

	public void insertFirst(T data)
	{
		Node<T> newNode = new Node<T>(data);
		newNode.next = head;
		head = newNode;
		count++;
	}

	public void insertLast(T data)
	{

		if(count == 0)
		{
			insertFirst(data);
		}
		else
		{
			Node<T> newNode = new Node<T>(data);

			Node<T> current = head;
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

	public T peekFirst()
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

	public T peekLast()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else
		{
			Node<T> current = head;
			while(current.next != null)
			{
				current = current.next;
			}
			return current.data;
		}
	}

	public T removeFirst()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else
		{
			Node<T> firstNode = head;
			head = firstNode.next;
			count--;
			return firstNode.data;
		}

	}

	public T removeLast()
	{
		if(isEmpty())
		{
			throw new ArrayIndexOutOfBoundsException("Linked List is empty.");
		}
		else if(count == 1)
		{
			T onlyValue = removeFirst();
			count--;
			return onlyValue;
		}
		else
		{
			Node<T> current = head;
			Node<T> previousNode = null;
			while(current.next != null)
			{
				previousNode = current;
				current = current.next;
			}
			Node<T> lastNode = current;
			previousNode.next = null;
			count--;
			return lastNode.data;
		}
	}

	public int count()
	{
			return count;
	}

	public Iterator<T> iterator()
	{
		return  new myLinkedListIterator<T>(this);
	}

	private class myLinkedListIterator<T> implements Iterator
	{
		private Node<T> iterNext;
		public myLinkedListIterator(LinkedList theList)
		{
			iterNext = theList.head;
		}

		public boolean hasNext()
		{
			return (iterNext != null);
		}

		public T next()
		{
			T value;
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
