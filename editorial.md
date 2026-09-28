**Problem Editorial for D-ary Codes**

D-ary Huffman coding is a variation of the Huffman code from lecture 12.

The standard Huffman code algorithm builds a full binary tree out of symbols sorted by frequency using a priority queue (usually implemented with a binary heap). A full binary tree requires that every node in the tree has exactly 2 children, unless it is the tree consisting of a single root node, which has 0 children.

Extending the Huffman code to an alphabet of d symbols requires us to build a full $d$-ary tree, where each node has exactly 0 or $d$ children. Every merge step should merge two full $d$-ary trees; we can think of the associated data structure as a $d$-ary heap.

The key observation is that in the general case, we must add 'dummy' symbols with frequency 0.

The smallest $d$-ary tree is just a root node, which has 1 leaf node. Adding $d$ children to a $d$-ary tree increases the number of leaves by $(d-1)$, since the parent node is no longer a leaf.

Therefore, the number of leaf nodes $n$ in a full $d$-ary tree with $k$ non-leaf nodes will be:

$n = 1 + k(d-1) \quad$ for integer $k=0,1,2,\dots$

If we subtract the 1 from both sides, we realise:

$(n-1) \mod (d-1) = 0.$

Hence if we have N symbols in our string where (n-1) mod (d-1) != 0, then we have to pad the heap with dummy symbols:

$\#(\text{dummy symbols to add}) = (d-1) - (n-1) \mod (d-1).$

Instead of actually building a d-ary heap, we can use a binary heap and extract the minimum value d times for each merge operation. The number of merges that a symbol is involved in is the length of the optimal variable-length code.
