# Python Dev Notes

## Lists vs Tuples
* Tuples are more lightweight and usually preferable when data becomes static. 
* The `list.append` function over-allocates space to the list (the assumption is that one append is the precursor of many appends). Therefore, it's possible to grow lists to be much larger than intended. 
* Not storing additional headroom by creating new tuples instead of appending has the advantage of not overallocating memory, but it may be slower if done repeatedly as the new allocation happens every time you want to grow a tuple. 
* Lists are larger than tuples even without `.append` as they have to keep track of a lot more information. 
* Python can also create tuples via resource caching - this means that tuples of size 1-20 aren't immediately garbage collected but saved for later use. The end result is that when a new tuple of the same size is needed in the future, we don't need to communicate with the operating system in order to find spare memory - it's already allocated. 

