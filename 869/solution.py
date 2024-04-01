class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numerals = list(str(n))
        digits = len(numerals)
        candidates = []
        power = 0
        
        #get all powers of 2 until the number digits = number of digits in n
        def power_stack(digits, stack, power):
            exponential = 2**power
            if len(list(str(exponential))) > digits:
                return stack
            elif len(list(str(exponential))) == digits:
                stack.append(list(str(exponential)))
                return power_stack(digits, stack, power+1)
            else:
                return power_stack(digits, stack, power+1)
        
        #the number of digits match, so check and see if all of the same digits are there
        def check_list(target_list, numerals):
            if not target_list:
                return False
            target = target_list.pop()
            if not any([t for t in target if t not in numerals]):
                if check(target, numerals):
                    return True
            else:
                return check_list(target_list, numerals)
        
        def check(target, numerals):
            if not target:
                if not numerals:
                    return True
                else:
                    return False
            else:
                num = target.pop()
                if num in numerals:
                    i = numerals.index(num)
                    return check(target, [x for j, x in enumerate(numerals) if i != j])
                return check(target, numerals)
            
        
        targets = power_stack(digits, candidates, power)
        if not targets:
            return False
        return check_list(targets, numerals)