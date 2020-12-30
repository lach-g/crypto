public class ListTest
{
	public static void main(String args[])
	{
		LinkedList testList = new LinkedList();
		//System.out.println(testList.isEmpty());
		// testList.insertLast(1);
		// testList.insertLast(2);
		// testList.insertLast(3);
		// testList.insertLast(4);
		// testList.insertFirst(0);
		// testList.display();
		// System.out.println(testList.isEmpty());
		// System.out.println(testList.peekFirst());
		// System.out.println(testList.peekLast());
		// System.out.println(testList.removeFirst());
		// System.out.println(testList.removeLast());
		// System.out.println(testList.count());

		Stats stock1 = new Stats();
		stock1.mean = 50;
		stock1.max = 100;
		stock1.min = 0;

		Stats stock2 = new Stats();
		stock2.mean = 500;
		stock2.max = 1000;
		stock2.min = 2;

		LinkedList objectTestList = new LinkedList();
		objectTestList.insertFirst(stock1);
		objectTestList.insertLast(stock2);


		// for(Object o : testList)
		// {
		// 	System.out.println(o);
		// }
	}
}

