AI Usage Statement (28 September 2026)

```text
I used AI (Microsoft CoPilot) as a discussion partner during the design and validation of the programming contest problem.

The discussion focused on:

- Generalizing Huffman coding from binary to arbitrary dd-ary alphabets.
- The requirement to add dummy zero-frequency symbols so that the number of leaves satisfies (n−1) mod (d−1)=0.(n-1)\bmod(d-1)=0.
- The observation that the total encoded length can be computed directly during Huffman's algorithm as the sum of all merge costs, without explicitly constructing codewords.
- The distinction between a dd-ary Huffman code and a dd-ary heap. A dd-ary Huffman code does not require a dd-ary heap; any priority queue implementation (including a standard binary heap) is sufficient.
- The difficulty of implementing binary, ternary, and general dd-ary heaps, and whether the proposed contest problem would naturally require contestants to implement a dd-ary heap.
- The conclusion that the problem primarily tests understanding of generalized Huffman coding and priority queues rather than heap implementation, unless additional constraints are introduced.

The AI also assisted in manually checking a worked example for correctness, but the final problem concept, statement, and design decisions were made by me.
```