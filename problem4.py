max_palindrome = -1

for num1 in range(100,1000):
    for num2 in range(100,1000):
        product = num1 * num2
        string_product = str(product)
        string_product_length = len(string_product)
        #check if palindrome
        is_palindrome = True
        for i in range(0, string_product_length/2):
            if(string_product[i] != string_product[string_product_length-i-1]):
                is_palindrome = False
                break
        if(is_palindrome == True and product > max_palindrome):
            max_palindrome = product

print "max palindrome is " + str(max_palindrome)