    def selfDividingNumbers( left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right+1) if all((int(d) and not num % int(d)) for d in str(num))]

    
      def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left,right+1):
            if(self.isSelfDividingNumber(num)):
                result.append(num)
        return result
    def isSelfDividingNumber(self, num):
        num_str = str(num)
        if '0' in num_str:
            return False
        else:
            return all(num % int(i) == 0 for i in num_str)

        
