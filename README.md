# Crypto Graph

Crypto Graph is a python package that implements a variety of data structures and algorithms to analyse crypto-currency trading data.

## Requirements

- __numpy__: used for arrays
- __requests__: used for the api
- __math__: used for the hashing algorithm
- __pickle__: used to save the current market data structure
- __csv__: used to read from csv files
- __sys__: used to refresh command line
- __os__: used to find correct working directory of file
- __json__: used to parse the api response
- __unittest__: used to test all functionality

## Usage

For report mode:
```bash
python3 cryptoGraph.py -r assets.csv trades.csv
```
For interactive mode:
```bash
python3 cryptoGraph.py -i
```
Unit tests:
```bash
python3 -m unittest discover test
```

## Contents

### Python files
- init.py: Allows access to different directories
- assetClass.py: Contains the class definition of an asset object along with functionality to display it to the command line
- cryptoGraph.py: Contains the main function of the package
- currentMarketClass.py: Contains the class definition of a current market object and all functions related to its manipulation
- dataGrabClass.py: Contains the class definition of a data grab object for parsing and loading .csv files into a current market object
- DoubleLinkedList_dsa.py: Data Structure written and previously submitted, used for it's iterative expanding capabilities
- Graph_dsa.py: Data Structure written and previously submitted, used for traversals of trading data
- HashTable_dsa.py: Data Structure written and previously submitted, used for O(1) lookups of Asset and Trade objects
- LinkedList_dsa.py: Data Structure written and previously submitted, used as a lighter weight alternative to the Double Linked List
- menu.py: Contains the class definition of a menu object that prints command line instructions, takes user input and directs it to the appropriate functions
- Pickling.py: Class has been previously submitted, it is used here for saving and loading the current market object
- Queue_dll_dsa.py: Data Structure written and previously submitted, it is used for the first in first out functionality during traversals
- Stack_dll_dsa.py: Data Structure written and previously submitted, it is used for the last in first out functionality during traversals
- tradeClass.py: Contains the class definition of a trade object along with functionality to display it to the command line
- test/init.py: Allows access to different directories
- test/test_assetClass.py: Unit test for the Asset Class
- test/test_currentMarketClass.py: Unit test for the Current Market Class
- test/test_dataGrab.py: Unit test for the Data Grab Class
- test/test_DoubleLinkedList.py: Unit test for the Double Linked List Class
- test/test_Graph.py: Unit test for the Graph Class
- test/test_HashTable.py: Unit test for the Hash Table Class
- test/test_LinkedList.py: Unit test for the Linked List Class
- test/test_Pickling.py: Unit test for the Pickling Class
- test/test_Queue.py: Unit test for the Queue Class
- test/test_Stack.py: Unit test for the Stack Class
- test/test_tradeClass.py: Unit test for the Trade Class

### CSV files
- assets.csv: The asset data provided, which the package parses and internally analyses keeping the files unmodified
- trades.csv: The trade data provided, which the package parses and internally analyses keeping the files unmodified

### ODT files
- project_report.odt: The Report required for the DSA Assignment

## Version Information
21/01/2021 - initial version of the Crypto Graph package