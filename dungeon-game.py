minm = float('-inf')
d1 = []
d2 = []
class Solution:
   def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        xt = len(dungeon) - 1
        yt = len(dungeon[0]) - 1
        def find(self, x, y, current, tt, move):
            global minm, d1, d2
            if x == xt and y == yt:
                tt += dungeon[x][y]
                current = min(current, tt)
                minm = max(current, minm)
                return
            else:
                if move in d1:
                    tm = d1.find(move)
                    current = d2[tm][0]
                    tt = d2[tm][1]
                else:
                    tt += dungeon[x][y]
                    current = min(current, tt)
                    d1.append(move)
                    d2.append([current, tt])
                    
                if current <= minm:
                    return
                if x < xt and y < yt:
                    find(self, x+1, y, current, tt, move+[(x+1, y)])
                    find(self, x, y+1, current, tt, move+[(x, y+1)])
                elif x<xt:
                    find(self, x+1, y, current, tt, move+[(x+1, y)])
                elif y<yt:
                    find(self, x, y+1, current, tt, move+[(x, y+1)])

        global minm, d1, d2
        d2 = []
        d1 = []
        minm = float('-inf')
        find(self, 0, 0, 0, 0, [(0,0)])
        print(d1, d2)
        return max(minm*(-1) + 1, 0)
