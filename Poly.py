#  File: Poly.py

#  Description: There are 2 main functions. You add 2 polynomials. You multiply 2 polynomials. Both is acheived through linked list

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Partner Name: Saivachan Ponnapalli

#  Partner UT EID: sp48347

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/31/2022

#  Date Last Modified: 10/31/2022

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        # first case if for when linked list is empty
        # second case is for inserting in decsending order based on the exponents
        if self.first == None:
            new_link = Link(coeff, exp)
            self.first = new_link
        elif exp > self.first.exp:
            temp = self.first
            new_link = Link(coeff, exp, temp)
            self.first = new_link
        else:
            current = self.first
            while current != None:
                if current.next == None:
                    break
                if current.exp >= exp and current.next.exp < exp:
                    new_link = Link(coeff, exp, current.next)
                    current.next = new_link
                    return
                else:
                    current = current.next
            new_link = Link(coeff, exp)
            current.next = new_link


    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        combined = LinkedList()
        # The first 3 if statements take care of the base cases of when both or either list is empty
        if self.first == None and p.first == None:
            return combined
        if self.first == None:
            return p
        if p.first == None:
            return self
        current = self.first
        # These 2 loops inserts the polynomials into a new linked list in order
        while current != None:
            combined.insert_in_order(current.coeff, current.exp)
            current = current.next
        current = p.first
        while current != None:
            combined.insert_in_order(current.coeff, current.exp)
            current = current.next
        current = combined.first
        # This loop adds together coefficients that have the same exponent
        while current.next != None:
            if current.exp == current.next.exp:
                current.coeff = current.coeff + current.next.coeff
                current.next = current.next.next
            else:
                current = current.next

        return combined

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        combined = LinkedList()
        # The first 3 if statements take care of the base cases of when both or either list is empty
        # The else statement multiplies the 2 polynomonials and inserts them in order in the new list
        # coefficients with the same exponent are added
        if self.first == None and p.first == None:
            return combined
        elif self.first == None:
            return p
        elif p.first == None:
            return self
        else:
            currentq = self.first
            while currentq != None:
                currentp = p.first
                while currentp != None:
                    new_coeff = currentq.coeff * currentp.coeff
                    new_exp = currentq.exp + currentp.exp
                    combined.insert_in_order(new_coeff, new_exp)
                    currentp = currentp.next
                currentq = currentq.next
            current = combined.first
            while current.next != None:
                if current.exp == current.next.exp:
                    current.coeff = current.coeff + current.next.coeff
                    current.next = current.next.next
                else:
                    current = current.next
            return combined


    # create a string representation of the polynomial
    def __str__ (self):
        string = ""
        current = self.first
        if current == None:
            return string
        while current.next != None:
            if current.coeff != 0:
                string += "(" + str(current.coeff) + ", " + str(current.exp) + ") + "
            current = current.next
        if current.coeff != 0:
            string += "(" + str(current.coeff) + ", " + str(current.exp) + ")"
        if string[-3:] == " + ":
            string = string[:-3]
        return string

def main():
    # read data from file poly.in from stdin
    data = sys.stdin
    # create polynomial p
    p = LinkedList()
    for i in range(int(data.readline().strip())):
        line = data.readline().strip()
        lst = line.split()
        p.insert_in_order(int(lst[0]), int(lst[1]))
    data.readline().strip()
    # create polynomial q
    q = LinkedList()
    for i in range(int(data.readline().strip())):
        line = data.readline().strip()
        lst = line.split()
        q.insert_in_order(int(lst[0]), int(lst[1]))
    # get sum of p and q and print sum
    print(p.add(q))
    # get product of p and q and print product
    print(p.mult(q))

if __name__ == "__main__":
    main()