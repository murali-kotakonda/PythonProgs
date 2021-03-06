# Collections -->> Data Structures --->
# to hold multiple data
"""
Collections/Data Structures:
--------------------------------
- is a variable that internally can maintain/store multiple data.
->Is required when we have large group of data.
-> collecting and manipulating a group of objects.
->Operations : searching, sorting, insertion, manipulation, deletion, updation.

collection supported in python:
---------------------------
-> List
->Tuple
->Set
->Dictionary

# Collection    Index     Insertion order   Allow Duplicates?   Mutuable   Represent                  searchByposition         searchBycontent
# List -        Yes           Yes             Yes                Yes          []                         Yes(fast)				 yes(slow)
# Tuple -       Yes           Yes             Yes                No           ()                         Yes(fast) 				 yes(slow)
# Set  -        No            No              No                 Yes          {}                            NA					 yes(fast)
# Dictionary -  No            No              No                 Yes          {}with key + value            NA					 yes(fast)


Index --> 
position based operations
insert/delete/update/read based on positions.
position starts from 0
1st element is added at 0 position.
2nd element is added at 1 position.
list and tuple supports the index based operations.
........


Insertion order:
The order in which the elements are added === the order in which the elements are stored.
add: 50 , 60 , 10 , 67 , 100, 3
supported for list and tuple
Read:
List/ Tuple o/p: 50 , 60 , 10 , 67 , 100, 3
Set/Dict  : 60 , 50 ,  100, 3 ,  67  ,10
[Set/Dict  stores the elements in random order.]


Allow duplicates:
List and Tuple will allows duplicates.
Set and dict avoids duplicates.
ex: ADD "kumar" ,"kumar"  "kumar"
List/Tuple : the no of elements is 3
Set/Dict : the no of elements is 1 [no duplicate elements.]


Mutuable:
can it be changed or altered ( add new element/ update existing / delete existing )
Tuple is Immutuable ,once created it cannot be changed.


syntax for creating a variable:
-----------------------------
List:
data = [] or data = list()

Tuple
data = () or data = tuple()

Set
data = {} or data = set()

Dictionay
data = dict()


Req1: [search by position ]
collection has 500 elements ,get element at 400 position
use: list or tuple

Req2: [search by content]
collection has 500 cities ,check if "london" exists
use: set or dict
"""