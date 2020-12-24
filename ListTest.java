public class ListTest
{
	public static void main(String args[])
	{
		LinkedList testList = new LinkedList();
		System.out.println(testList.isEmpty());
		testList.insertLast(1);
		testList.insertLast(2);
		testList.insertLast(3);
		testList.insertLast(4);
		testList.insertFirst(0);
		testList.display();
		System.out.println(testList.isEmpty());
		System.out.println(testList.peekFirst());
		System.out.println(testList.peekLast());
		System.out.println(testList.removeFirst());
		System.out.println(testList.removeLast());
		System.out.println(testList.count());

	}
}