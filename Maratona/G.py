from tkinter.messagebox import RETRY

# x e y são as coordenadas e k é o index da letra atual:
def deepSearchWord(grid, word, x, y, k, direction):
    if(k >= len(word)):
        return True
    k += 1
    if direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    elif direction == ''

    if grid[x][y] == 'U':
        dire


def searchWord(grid, word):
    for i in range(grid):
        for j in range(grid[i]):
            if grid[i][j] == word[0]:
                return deepSearchWord(grid, word, i, j, 0, 'U') + deepSearchWord(grid, word, i, j, 0, 'L') + deepSearchWord(grid, word, i, j, 0, 'R') + deepSearchWord(grid, word, i, j, 0, 'D') 

n, m = input().split('')
grid = []
for i in range(n):
    word = input()
    row = []
    for letter in word:
        row.append(letter)
    grid.append(row)

q = input()
words = []
for i in range(q):
    word = input()
    words.append(word)

#for word in words: