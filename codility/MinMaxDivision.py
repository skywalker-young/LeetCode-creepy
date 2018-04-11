def blocksNo(A, maxBlock):
    # Initially set the A[0] being an individual block
 
    blocksNumber = 1    # The number of blocks, that A could
                        # be divided to with the restriction
                        # that, the sum of each block is less
                        # than or equal to maxBlock
    preBlockSum = A[0]
 
    for element in A[1:]:
        # Try to extend the previous block
        if preBlockSum + element > maxBlock:
            # Fail to extend the previous block, because
            # of the sum limitation maxBlock
            preBlockSum = element
            blocksNumber += 1
        else:
            preBlockSum += element
 
    return blocksNumber
 
def solution(K, A):
    blocksNeeded = 0    # Given the restriction on the sum of
                        # each block, how many blocks could
                        # the original A be divided to?
    resultLowerBound = max(A)
    resultUpperBound = sum(A)
    result = 0          # Minimal large sum
 
    # Handle two special cases
    if K == 1:      return resultUpperBound
    if K >= len(A): return resultLowerBound
 
    # Binary search the result
    while resultLowerBound <= resultUpperBound:
        resultMaxMid = (resultLowerBound + resultUpperBound) / 2
        blocksNeeded = blocksNo(A, resultMaxMid)
        if blocksNeeded <= K:
            # With large sum being resultMaxMid or resultMaxMid-,
            # we need blocksNeeded/blocksNeeded- blocks. While we
            # have some unused blocks (K - blocksNeeded), We could
            # try to use them to decrease the large sum.
            resultUpperBound = resultMaxMid - 1
            result = resultMaxMid
        else:
            # With large sum being resultMaxMid or resultMaxMid-,
            # we need to use more than K blocks. So resultMaxMid
            # is impossible to be our answer.
            resultLowerBound = resultMaxMid + 1
 
    return result
