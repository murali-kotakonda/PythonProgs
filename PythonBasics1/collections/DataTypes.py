# Collections -->> Data Structures --->
# to hold multiple data
"""
Collections/Data Structures:
--------------------------------
->Is required when we have large group of data.
-> collecting and manipulating a group of objects.
->Operations : searching, sorting, insertion, manipulation, deletion, updation.
-> List
->Tuple
->Set
->Dictionary

#               Index     Insertion order   Allow Duplicates?   Mutuable   Represent                  searchByposition         searchBycontent
# List -        Yes           Yes             Yes                Yes          []                         Yes(fast)				 yes(slow)
# Tuple -       Yes           Yes             Yes                No           ()                         Yes(fast) 				 yes(slow)
# Set  -        No            No              No                 Yes          {}                            NA					 yes(fast)
# Dictionary -  No            No              No                 Yes          {}with key + value            NA					 yes(fast)


Index --> position based operations
insert/delete/update/read based on positions.
position starts from 0
1st element is added at 0 position.
2nd element is added at 1 position.
........


Insertion order:
The order in which the elements are added === the order in which the elements are stored.
add: 50 , 60 , 10 , 67 , 100, 3
Read: List/ Tuple o/p: 50 , 60 , 10 , 67 , 100, 3
Set/Dict stores the elements in random order.



Mutuable:
can it be changed or altered ( add new element/ upddate existing / delete existing )
Tuple is immutabled. once creaed it cannot be changed,

List:
data = [] or data = list()

Tuple
data = () or data = tuple()

Set
data = {} or data = set()

Dictionay
data = dict()



"""