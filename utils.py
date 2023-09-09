class utils:
    def reversed(self, num):
        if not isinstance(num, int):
            print(f"Error! Expecting input of type int")
            return None
        
        result = 0
        while num:
            digit = num%10
            result = result*10 + digit
            num //= 10
        return result
    
    def formatter(self, num):
        if not isinstance(num, int):
            print(f"Error! Expecting input of type int")
            return None
        
        binary_num = format(num, "b")
        octal_num = format(num, "o")
        print(binary_num, octal_num)
        return (binary_num,octal_num)
