# CITS3001: Build Your Own Programming Contest
A collection of programming problems in the problemtools format.

## Project Requirements
Each person in the team is to submit 1 programming problem using the [problemtools](https://github.com/Kattis/problemtools) directory format. Note that we are using the [Legacy (ICPC) version](https://www.kattis.com/problem-package-format/spec/legacy-icpc.html#problem-statements).

```
sample-problem-grumpyqueue
├── data
│   ├── sample
│   │   ├── 1.ans
│   │   ├── 1.in
│   │   ├── 2.ans
│   │   └── 2.in
│   └── secret
│       ├── 01_sorted.ans
│       ├── 01_sorted.in
│       ├── 02_reverse.ans
│       ├── 02_reverse.in
│       ├── 03_random_max.ans
│       ├── 03_random_max.in
│       ├── 04_single.ans
│       ├── 04_single.in
│       ├── 05_all_equal.ans
│       └── 05_all_equal.in
├── domjudge-problem.ini
├── problem_statement
│   └── problem.en.tex
├── problem.yaml
└── submissions
    ├── accepted
    │   └── solution.py
    ├── time_limit_exceeded
    │   └── tle.py
    └── wrong_answer
        └── wa.py
```
Each programming problem should have the following:
1. Title, capturing the essence of the story
2. Description `problem.en.tex`: sets the problem in some story, with a precise specification of input and output format
3. Set of Python solution files in `submissions/`
    1. Correct solution: `accepted/solution.py`
    2. Naive solution(s) which fail due to time out: `time_limit_exceeded/tle.py`
    3. Incorrect solution(s) giving wrong answers due to false assumptions: `wrong_answer/wa.py`
4. Sample data in `data/sample` following your specification to test correctness
5. Additional secret test data in `data/secret` to test correctness of submission
6. Meta-data listing time limits and other context (`problem.yaml`). See [ICPC examples](https://icpc.io/problem-package-format/examples/problem_yaml)

Additionally, each person in the team must produce a 1 page solution description / editorial with:
- High level description of the intended solution
- Time and space complexity analysis
- Declaration of any AI use in building the problem and solution

Students should submit their problemtools directory as a zipped file `problem-XX-NNNNNNNN.zip` on LMS, where `XX` is the group number (36) and `NNNNNNNN` is the student number. The individual submissions are due by October 2.

### Group Assessment
Students are required to complete attempts and assessments of each other's problems by October 9th, via FeedbackFruits.

Each person must provide, for each other group member's problem:
1. At least 1 attempted solution (it does not need to be correct). Spend around an hour on this.
2. A critical assessment of the difficulty of that problem, and suggestions for improvement.

### Use of Artificial Intelligence
Students must not submit any AI generated code or text in this assignment. Students may use AI assistants for ideas, suggestions for debugging, and identifying algorithmic strategy, but all submissions must be the original work of the student.

All students should submit an honest account of how AI was used in their work. Additionally, any sources used for research/inspiration should be cited.

## Examples

### TeX Example
```tex
\problemname{The Grumpy Queue}

People are queueing for coffee. A person is \emph{grumpy} if the person
{\em directly} in front of them is taller than they are --- they can't see the
menu. Count the number of grumpy people.

\section*{Input}
The first line contains an integer $n$ ($1 \le n \le 10^6$), the number
of people. The second line contains $n$ integers $h_1, \dots, h_n$
($0 \le h_i \le 10^9$), the heights from the front of the queue to the
back.

\section*{Output}
Output a single integer: the number of positions $i$ ($1 \le i < n$)
with $h_i > h_{i+1}$.
```

*Note that the problem statement Tex file is only the body file. To compile the PDF, install problemtools and run on the problem directory: `problem2pdf sample-problem-grumpyqueue`*

### YAML Example
```yaml
problem_format_version: legacy-icpc
name: Guess the Number
uuid: 5ca6ba5b-36d5-4eff-8aa7-d967cbc4375e
author: John von Judge
source: Kattis
license: cc by-sa

# Default limit values
# You can set a fixed time limit or a multiplier of accepted solution
limits:
  #time_limit: 3.0
  time_multiplier: 5.0
  #time_safety_margin: 2.0
  memory: 2048
  output: 8
  code: 128
  compilation_time: 60
  compilation_memory: 2048
  validation_time: 60
  validation_memory: 2048
  validation_output: 8
```

See also the [DOMJudge problem format specification](https://www.domjudge.org/docs/manual/7.3/problem-format.html) for details on `domjudge-problem.ini`

## Marking Scheme

| Component                 | Weight  | Description |
|---------------------------|---------|-------------|
| **Problem Quality**       | **40%** |             |
| Algorithm and description | 15%     | Well chosen algorithm and creative description that does not make the intended solution obvious. Clear sample data that helps the reader understand the challenge |
| Solutions                 | 10%     | Set of intended solutions plus non-accepting solutions in Python, clearly commented and demonstrating good coding practice |
| Test data                 | 10%     | Well-designed test data that clearly differentiates intended and non-accepting solutions. Cover edge cases and include randomised test data at input limits
| Meta data                 | 5%      | Problemtools format applied correctly, with `problem.yaml` specifying time and memory limits |
| **Solutions Description** | **30%** |             |
| Overview                  | 10%     | Summary of the problem, relating to algorithms/techniques covered in lectures. Explains key insights required to solve the problem |
| Solution                  | 10%     | Pseudocode of algorithm and description of data structures used in solution. Clear and easy to follow. Highlight when alternative approaches will not work |
| Complexity analysis       | 10%     | Derive the time and space complexity of the intended solution. Should roughly agree with the test data |
| **Peer Problem Attempts** | **20%** |             |
| Attempted solution        | 10%     | Aim to spend at most one hour on each problem, and provide the code of your attempt  |
| Feedback                  | 10%     | For each group member, provide a paragraph giving constructive feedback on their problem. What you liked, and what you had trouble understanding |
| **Teamwork Score**        | **10%** |             |
| Contest quality           | 5%      | A well designed contest without repetition and spectrum of easy (less than 10 minutes to solve) to challenging (45-60 minutes to solve) |
| Team dynamics             | 5%      | Everyone worked well together, problems were provided with sufficient feedback, and feedback was thoughtful and professional |