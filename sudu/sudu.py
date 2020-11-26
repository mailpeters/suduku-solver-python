
from array import *

block = [
        [[1], [1], [1], [2], [2], [2], [3], [3], [3]],
        [[1], [1], [1], [2], [2], [2], [3], [3], [3]],
        [[1], [1], [1], [2], [2], [2], [3], [3], [3]],
        [[4], [4], [4], [5], [5], [5], [6], [6], [6]],
        [[4], [4], [4], [5], [5], [5], [6], [6], [6]],
        [[4], [4], [4], [5], [5], [5], [6], [6], [6]],
        [[7], [7], [7], [8], [8], [8], [9], [9], [9]],
        [[7], [7], [7], [8], [8], [8], [9], [9], [9]],
        [[7], [7], [7], [8], [8], [8], [9], [9], [9]]]


# remove 9 from 0,0
answer = [
        [[], [8], [3], [6], [1], [7], [5], [4], [2]],
        [[7], [2], [4], [8], [9], [5], [3], [1], [6]],
        [[1], [5], [6], [2], [3], [4], [8], [9], [7]],
        [[2], [4], [9], [5], [6], [8], [7], [3], [1]],
        [[5], [3], [7], [1], [4], [9], [2], [6], [8]],
        [[8], [6], [1], [3], [7], [2], [9], [5], [4]],
        [[3], [7], [5], [4], [8], [6], [1], [2], [9]],
        [[6], [1], [8], [9], [2], [3], [4], [7], [5]],
        [[4], [9], [2], [7], [5], [1], [6], [8], [3]]]



# board = [
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []],
#         [[], [], [], [], [], [], [], [], []]]
#
#


#aSolve = board

board = [
        [[], [8], [], [], [], [], [5], [], [2]],
        [[], [], [], [], [], [], [3], [], [6]],
        [[], [5], [], [], [], [], [], [9], []],
        [[2], [], [], [5], [], [], [], [], [1]],
        [[], [3], [7], [1], [], [9], [], [], []],
        [[8], [6], [], [], [], [], [], [], []],
        [[3], [], [], [], [8], [], [], [], []],
        [[], [], [], [9], [2], [], [], [7], []],
        [[], [9], [], [], [5], [], [6], [8], []]]



board = [
        [[9], [], [] , [],  [], [],  [],  [],  [5]],
        [[5], [], [],  [7], [], [9], [],  [],  []],
        [[4], [1], [], [8], [], [],  [],  [],  [7]],
        [[],  [], [7], [2], [], [],  [9], [],  []],
        [[8], [], [],  [9], [], [6], [],  [],  [2]],
        [[],  [], [2], [],  [], [5], [4], [],  []],
        [[7], [], [],  [],  [], [1], [],  [5], [8]],
        [[],  [],  [],  [3], [], [4], [],  [],  [9]],
        [[1], [], [],  [],  [], [],  [],  [],  [3]]]




board = [
        [[],  [], [6],  [8], [5], [4], [],  [9], []],
        [[],  [], [7],  [9], [],  [],  [],  [],  []],
        [[],  [],  [],  [],  [6], [],  [],  [],  [5]],
        [[1], [4], [3], [7], [],  [5], [],  [],  []],
        [[2], [],  [],  [3], [],  [],  [],  [],  []],
        [[8], [],  [],  [],  [],  [],  [],  [],  [4]],
        [[],  [],  [],  [],  [1], [],  [2], [],  []],
        [[],  [],  [],  [5], [],  [9], [],  [],  []],
        [[6], [1], [],  [],  [],  [],  [],  [8], []]]


# remove 3
answer = [
        [[3], [2], [6], [8], [5], [4], [1], [9], [7]],
        [[4], [5], [7], [9], [3], [1], [6], [2], [8]],
        [[9], [8], [1], [2], [6], [7], [3], [4], [5]],
        [[1], [4], [3], [7], [8], [5], [9], [6], [2]],
        [[2], [7], [9], [3], [4], [6], [8], [5], [1]],
        [[8], [6], [5], [1], [9], [2], [7], [3], [4]],
        [[5], [9], [4], [6], [1], [8], [2], [7], [3]],
        [[7], [3], [8], [5], [2], [9], [4], [1], [6]],
        [[6], [1], [2], [4], [7], [3], [5], [8], [9]]]




# clears out the possibilites for cells with more than 1 value
def Iterrate():

    for r in range(0, 9):
        for c in range(0, 9):
            if len(board[r][c]) != 1:
                board[r][c] = []



def FillPossiblesLoop() :

    FillInPossibles()

    nSolves = CountSolves()
    print("first pass solved", nSolves)

    SolvedPrint()

    while True:

        Iterrate()

        FillInPossibles()

        nNewSolves = CountSolves()

        print("updated solved count ", nNewSolves)

        if nNewSolves > nSolves:
            nSolves=nNewSolves
        else:
            break



def FillInPossibles():

    # fill in possibles for every cell thats empty

    for r in range(0, 9):

        for c in range(0, 9):

            if board[r][c] == []:
                nCandidates = []

                for n in range(1, 10):
                    if not (IsValInColumn(n, c)) and not IsValInRow(n, r) and [n] not in WhatsInMyblock(r, c):
                            nCandidates.append(n)

                board[r][c] = nCandidates



def QualityCheck() :

    #return True

    print("in quality")
    lError = False

    for n in range(1,10):

        # how many times is each number found in a row

        for r in range(0, 9):
            nCount = 0

            for c in range(0, 9):

                if len(board[r][c]) == 0:
                    print("EMPTY ERROR found at", r, c)
                    lError = True

                # only apply this if the answer grid is filled out
                if answer[0][0] != []:
                    if len(board[r][c])==1 and (answer[r][c] != board[r][c]) :
                        print("ERROR WRONG VALUE",board[r][c],"found at", r, c)
                        lError = True

                # a single value in the cell and it matches current candidate
                if len(board[r][c])==1 and board[r][c]==[n]:
                    nCount += 1
                    if nCount > 1:
                        print("DUPE ERROR found twice in ROW", n , "found at", r,c)
                        lError=True


        # how many times is each number found in a column
        for c in range(0, 9):
            nCount = 0

            for r in range(0, 9):

                # a single value in the cell and it matches current candidate
                if len(board[r][c]) == 1 and board[r][c] == [n]:
                    nCount += 1
                    if nCount > 1:
                        print("DUPE ERROR found twice in COLUMN", n, "found at", r, c)
                        lError=True


    return lError



# find naked pairs in a column
def NakedPair():

    print("***************** naked pair")

    # for r in board:
    #     print(r)

    lRemovals = False

    #("naked pair COLUMN search")

    for c in range(0, 9):

        # nPairColumn = 0
        aPairFound = []

        for r in range(0, 9):

            if len(board[r][c]) == 2:

                if not board[r][c] in aPairFound:
                    # this means you found a pair of numbers
                    aPairFound.append(board[r][c])

                else:
                    # you found the same pair again
                    #print("found naked pair in column", board[r][c], r, c)

                    # found naked pair in a column, remove those values in the pair elsewhere in the column
                    aSearchPair = board[r][c]


                    for xx in range(0, 9):
                        if board[xx][c] != aSearchPair:

                            if aSearchPair[0] in board[xx][c]:
                                print("naked pair remove found element0", aSearchPair[0], "in", board[xx][c], xx, c)
                                board[xx][c].remove(aSearchPair[0])
                                lRemovals = True


                            if aSearchPair[1] in board[xx][c]:
                                print("naked pair found element1", aSearchPair[1], "in", board[xx][c], xx, c)
                                board[xx][c].remove(aSearchPair[1])
                                lRemovals = True


                    # CleanBlock(r,c,aSearchPair)




        # if nPairColumn > 1:
        #     print("found",nPairColumn,"pairs in row", r)
        #
        # # print("pairs", aPairFound)
        #
        # nPairColumn = 0



    #("naked pair ROW search")

    for r in range(0, 9):
        #
        # nPairRow = 0
        aPairFound = []

        for c in range(0, 9):

            if len(board[r][c]) == 2:
                #print("row found pair", board[r][c], r, c)
                # nPairRow += 1

                if not board[r][c] in aPairFound:
                    aPairFound.append(board[r][c])
                else:
                    #print("found naked pair in ROW", board[r][c], r, c)

                    # found naked pair in a column, remove those values in the pair elsewhere in the column
                    aSearchPair = board[r][c]


                    for xx in range(0, 9):
                        if board[r][xx] != aSearchPair:

                            if aSearchPair[0] in board[r][xx]:
                                print("naked pair remove element0", aSearchPair[0], "in", board[r][xx], r, xx)
                                board[r][xx].remove(aSearchPair[0])
                                lRemovals = True


                            if aSearchPair[1] in board[r][xx]:
                                print("naked pair remove element1", aSearchPair[1], "in", board[r][xx], r, xx)
                                board[r][xx].remove(aSearchPair[1])
                                lRemovals = True

                   #CleanBlock(r,c,aSearchPair)


    # for r in board:
    #     print(r)

    print("end naked pair")

    return lRemovals





# use after solving any cell

def CleanUpBoard() :

    print("cleanupboard")

    lFound = False

    # for r in board:
    #     print(r)

    for r in range(0, 9):
            for c in range(0, 9):

                # for every solved cell
                if len(board[r][c])==1:

                    for clean in range(0,9):

                        if len(board[r][clean]) > 1:

                            if board[r][c][0] in board[r][clean]:
                                # remove the solved value from all other columns in that row if imbedded
                                print("success ROW cleanup", board[r][c], "in", board[r][clean], r, clean)
                                board[r][clean].remove(board[r][c][0])
                                lFound = True



    for c in range(0, 9):

        for r in range(0, 9):

            # for every solved cell
            if len(board[r][c]) == 1:

                for clean in range(0, 9):

                    if len(board[clean][c]) > 1:

                        if board[r][c][0]  in board[clean][c]:
                            # remove the solved value from all other columns in that row if imbedded
                            print("success COLUMN cleanup", board[r][c], "in", board[clean][c], c, clean)
                            board[clean][c].remove( board[r][c][0] )
                            lFound = True


    # print()
    # for r in board:
    #     print(r)

    return lFound


def HiddenSingle():

    lFound = False

    print("***************************hidden single")

    # for r in board:
    #     print(r)


    # hidden single columns

    #print("start hidden single in ROW")
    for n in range(1, 10):

        # check in columns
        for r in range(0, 9):
            nPosition = -1
            nCount = 0

            # dont process if n is solved for row
            if not (IsValInRow(n, r)):

                for c in range(0, 9):

                    #print("*",r,c, board[r][c], n)

                    if len(board[r][c]) > 1:
                        #print("x", c, board[r][c], n)
                        if n in board[r][c]:
                            #print("test",r,c,board[r][c], n)
                            nCount += 1
                            nPosition = c

                # found only 1 appearance in column of n
                if nCount == 1:
                    print("found ROW hidden single of", n, "at row and position", r, nPosition, board[r][nPosition])
                    # solved, wipe out other options in that cell
                    board[r][nPosition] = [n]
                    lFound=True



    #
    # for r in board:
    #     print(r)


    #print("start hidden single in COLUMNS")
    for n in range(1, 10):

        # check in columns
        for c in range(0, 9):
            nPosition = -1
            nCount = 0

            # dont process if n is solved for row
            if not (IsValInColumn(n, c)):

                for r in range(0, 9):

                    if len(board[r][c]) > 1:
                        #print("x", c, board[r][c], n)
                        if n in board[r][c]:
                            #print("test",r,c,board[r][c], n)
                            nCount += 1
                            nPosition = r

                # found only 1 appearance in column of n
                if nCount == 1:
                    print("found COLUMN hidden single of", n, "at row and position", nPosition,c, board[nPosition][c])
                    # solved, wipe out other options in that cell
                    board[nPosition][c] = [n]
                    lFound=True



    # for r in board:
    #     print(r)

    # if lFound:
    #     CleanUpBoard()

    print("end hidden single")

    return lFound


def SolvedPrint():

    for r in range(0, 9):
        nRow = []

        for c in range(0, 9):
            if len(board[r][c]) == 1:
                nRow.append(board[r][c])
            else:
                nRow.append([0])

        print(r, nRow)



def CountSolves():

    nCount = 0

    for r in range(0, 9):
        for c in range(0, 9):
            if len(board[r][c]) == 1:
                nCount+=1


    return nCount


def CountPossibles():

    nCount = 0

    for r in range(0, 9):
        for c in range(0, 9):
            nCount = nCount + len(board[r][c])


    return nCount-81



def IsValInColumn(nVal,nCol):

    for r in board:
        # print(r[nCol])
        if r[nCol] == [nVal] :
            return True

    return False


def IsValInRow(nVal,nRow):

    for c in range(0,9):
        if len(board[nRow][c])== 1:
            if board[nRow][c] == [nVal]:
                return True

    return False



def WhatsInMyblock(nRow, nCol, nBlock=0):

    nReturn = []

    if nBlock ==0:

        if nRow < 3:
            rStart = 0
        elif nRow < 6:
            rStart = 3
        else:
            rStart = 6

        if nCol < 3:
            cStart = 0
        elif nCol < 6:
            cStart = 3
        else:
            cStart = 6

        for r in range(rStart, rStart + 3):
            for c in range(cStart, cStart + 3):
                if len(board[r][c] )==1:
                    nReturn.append( board[r][c] )

    else:

        for r in range(0,9):
            for c in range(0,9):
                if Block(r,c) == [nBlock]:
                    if len(board[r][c] )==1:
                        nReturn.append( board[r][c][0] )
                        # print("returning block")

    return nReturn


def Block(nRow, nCol):
    return block[nRow][nCol]


def TimesFoundInBlock(n,nBlock):

    nCount = 0

    # how many times is candidate in the block?
    for r in range(0, 9):
        for c in range(0, 9):

            # selected block only
            # value found in a cell
            # cell not solved
            if block[r][c] == [nBlock] and \
                    n in board[r][c] and  \
                        len( board[r][c]) > 1:
                nCount+=1

    return nCount




def TimesInARow(nVal, nRow):

    nCount= 0
    for c in range(0, 9):
        if nVal in board[nRow][c]:
            nCount +=1

    return nCount


def IsValueInRowOnlyInBlock(nVal, nRow, nBlock):

    nCount = 0
    for c in range(0, 9):

        # value found in row
        if nVal in board[nRow][c] :

            # value found in wrong block
            if block[nRow][c] != nBlock:
                nCount += 1

    return nCount


def TimesInAColumn(nVal, nCol):

    nCount = 0
    for r in range(0, 9):
        if nVal in board[r][nCol]:
            nCount += 1

    return nCount





# find Pointing pairs in a column
def PointingPair():

    print("***************** Pointing pair")
    #
    # for r in board:
    #     print(r)

    lRemovals = False

    #print("Pointing pair column search")

    for c in range(0, 9):

        # nPairColumn = 0
        aPairFound = []

        nBlock1 = 0
        nBlock2 = 0

        for r in range(0, 9):

            if len(board[r][c]) == 2:

                if not board[r][c] in aPairFound:
                    # this means you found a pair of numbers
                    aPairFound.append(board[r][c])
                    nBlock1 = Block(r,c)

                else:
                    # you found the same pair again
                    #print("found Pointing pair in column", board[r][c], r, c)
                    nBlock2=Block(r,c)

                    # found Pointing pair in a column, remove those values in the pair elsewhere in the column
                    aSearchPair = board[r][c]

                    # look for elements in in the other  columns
                    for xx in range(0, 9):
                        if board[xx][c] != aSearchPair:

                            if aSearchPair[0] in board[xx][c]:
                                print("pointing pair remove element0", aSearchPair[0], "in", board[xx][c], xx, c)
                                board[xx][c].remove(aSearchPair[0])
                                lRemovals = True


                            if aSearchPair[1] in board[xx][c]:
                                print("pointing pair remove element1", aSearchPair[1], "in", board[xx][c], xx, c)
                                board[xx][c].remove(aSearchPair[1])

                    # clean up the same block if the pairs are in the same block
                    if nBlock1==nBlock2:
                        CleanBlock(r, c, aSearchPair)

    #print("Pointing pair ROW search")

    for r in range(0, 9):
        #
        # nPairRow = 0
        aPairFound = []
        nBlock1 = 0
        nBlock2 = 0

        for c in range(0, 9):

            if len(board[r][c]) == 2:
                #print("row found pair", board[r][c], r, c)
                # nPairRow += 1

                if not board[r][c] in aPairFound:
                    aPairFound.append(board[r][c])
                    nBlock1 = Block(r,c)
                else:
                    #print("found Pointing pair in ROW", board[r][c], r, c)
                    nBlock2 = Block(r,c)

                    # found Pointing pair in a column, remove those values in the pair elsewhere in the column
                    aSearchPair = board[r][c]

                    for xx in range(0, 9):
                        if board[r][xx] != aSearchPair:

                            if aSearchPair[0] in board[r][xx]:
                                print("pointing pair element0", aSearchPair[0], "in", board[r][xx], r, xx)
                                board[r][xx].remove(aSearchPair[0])
                                lRemovals = True

                            if aSearchPair[1] in board[r][xx]:
                                print("pointing pair remove element1", aSearchPair[1], "in", board[r][xx], r, xx)
                                board[r][xx].remove(aSearchPair[1])
                                lRemovals = True

                    # clean up the same block if the pairs are in the same block
                    if nBlock1==nBlock2:
                        CleanBlock(r, c, aSearchPair)

    #
    # for r in board:
    #     print(r)

    print("end Pointing pair")

    return lRemovals




def CleanBlock(nRow, nCol, aSearchPair):

    # for r in board:
    #     print(r)
    print("************************CLEANBLOCK pair, row, col", aSearchPair, nRow,nCol)

    if nRow < 3:
        rStart = 0
    elif nRow < 6:
        rStart = 3
    else:
        rStart = 6

    if nCol < 3:
        cStart = 0
    elif nCol < 6:
        cStart = 3
    else:
        cStart = 6

    for r in range(rStart, rStart + 3):

        for c in range(cStart, cStart + 3):
            # address unsolved cells only

            if len(board[r][c] )!=1:

                # leave the exact match pairs intact
                if board[r][c] != aSearchPair:

                    if aSearchPair[0] in board[r][c]:
                        print("CLEANBLOCK search found element0", aSearchPair[0], "in", board[r][c], r, c)
                        board[r][c].remove(aSearchPair[0])
                        print( board[r][c],r,c)

                    if aSearchPair[1] in board[r][c]:
                        print("CLEANBLOCK search found element1", aSearchPair[1], "in", board[r][c], r, c)
                        board[r][c].remove(aSearchPair[1])
                        print( board[r][c],r,c)

    print("end cleanblock")



def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def HiddenSingleBlock() :

    print("************************ hidden single block ")

    aSolved = []

    for nBlock in range(1,10):

        aSolved = WhatsInMyblock(0,0,nBlock)
        #print(nBlock, "solved", aSolved)

        # remove the solved items from the possibles in the empty cells in the block

        # 9 means block is fully solved

        if len(aSolved) !=9:
            #print("block", nBlock,"not solved", aSolved)

            for r in range(0,9):

                for c in range(0, 9):

                    # find possibles
                    if Block(r,c) == [nBlock]:


                        # unsolved cell
                        if len(board[r][c]) != 1:


                            aRemoves = intersection(aSolved, board[r][c])
                            #print(aRemoves)
                            for xx in range(0,len(aRemoves)):
                                print("removing", aRemoves[xx], " from ",board[r][c], "block" , nBlock)
                                board[r][c].remove(aRemoves[xx])

    print("end hidden single block")


#****************************************************************


import timeit

start = timeit.timeit()

nSolves = CountSolves()
print("start", nSolves)

# fill array with possibles iteratively and start solving until no improvements made
FillPossiblesLoop()
QualityCheck()

nSolves = CountSolves()
print("final solves", nSolves)



while nSolves < 81 :

    print("************************************************************************************** top of loop")

    SolvedPrint()

    for r in board:
        print(r)

    nLastSolve = nSolves
    nLastPossible = CountPossibles()

    if nSolves < 81:

        print("starting hidden singles possible/solves", nLastPossible, nLastSolve)

        while HiddenSingle() :
            True

        nSolves = CountSolves()
        nPossibles = CountPossibles()

    if nSolves < 81:

        print("start CLEANUP possible/solves", nPossibles, nSolves)

        while CleanUpBoard() :
            True

        QualityCheck()


        nSolves = CountSolves()
        nPossibles = CountPossibles()


    if nSolves < 81:
        print("start naked pair possible/solves", nPossibles, nSolves)

        while NakedPair():
            True


        nSolves = CountSolves()
        nPossibles = CountPossibles()


    if nSolves < 81:
        print("start CLEANUP possible/solves", nPossibles, nSolves)

        while CleanUpBoard() :
            True

        QualityCheck()

        nSolves = CountSolves()
        nPossibles = CountPossibles()



    if nSolves < 81:
        print("start pointing pair possible/solves", nPossibles, nSolves)

        while PointingPair() :
            True

        QualityCheck()

        nSolves = CountSolves()
        nPossibles = CountPossibles()

    if nSolves < 81:

        print("start CLEANUP possible/solves", nPossibles, nSolves)

        while CleanUpBoard() :
            True

        nSolves = CountSolves()
        nPossibles = CountPossibles()


    if nSolves < 81:
        print("start HiddenSingleBlock possible/solves", nPossibles, nSolves)

        while HiddenSingleBlock():
            True

        nSolves = CountSolves()
        nPossibles = CountPossibles()

    print("bottom of loop possible/solves", nPossibles, nSolves)
    if nLastSolve==nSolves and nLastPossible == nPossibles:
        print("##################### no improvement, failure ############################")
        break


for r in board:
    print(r)

SolvedPrint()

end = timeit.timeit()
print("elapsed time", end - start)
