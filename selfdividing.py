    def selfDividingNumbers( left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right+1) if all((int(d) and not num % int(d)) for d in str(num))]

    
        def selfDividingNumbers(self, left, right):
        return [num for num in range(left, right + 1) if not any([digit == '0' or num % int(digit) != 0 for digit in str(num)])]
