# binary-full-adder
# Python program for Binary Full Adder

A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
Cin = int(input("Enter Carry-in (0 or 1): "))

# Full Adder logic
Sum = A ^ B ^ Cin
Carry = (A & B) | (B & Cin) | (A & Cin)

print("\nFull Adder Output:")
print("Sum =", Sum)
print("Carry =", Carry)

Example

Input:

Enter A (0 or 1): 1
Enter B (0 or 1): 1
Enter Carry-in (0 or 1): 0


Output:

Full Adder Output:
Sum = 0
Carry = 1

Full Adder Truth Table
A	B	Cin	Sum	Carry
0	0	0	0	0
0	0	1	1	0
0	1	0	1	0
0	1	1	0	1
1	0	0	1	0
1	0	1	0	1
1	1	0	0	1
1	1	1	1	1

Formula:

Sum = A XOR B XOR Cin

Carry = (A AND B) OR (B AND Cin) OR (A AND Cin)
