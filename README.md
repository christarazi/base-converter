# base-converter
Python3 program that can convert bases up to 36 including negative bases.

Inspired by <a href="http://www.reddit.com/r/dailyprogrammer/comments/2t3m7j/20150121_challenge_198_intermediate_basenegative/"> /r/dailyprogrammer</a> challlenge.

### Usage

*Note: The correct output is dependent on if the input is coherent. If not the program will behave unpredictably. 
Basically, you must be sure that the number you entered is in the correct base. The program will not know if the input doesn't make sense.*

Program takes 3 inputs from the command line:

1.  Number you want to convert
2.  The base of the number you entered 
3.  The base you want the output in


### Sample run

`$ python3.4 base_converter.py 7211 -10 10`
> `Input: 7211 base -10.`

> `Output: -6809 base 10.`
