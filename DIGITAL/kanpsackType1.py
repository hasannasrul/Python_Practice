#find maximum marks student score in a given interval of time 
def maxScore(marks,sec,n,totalSeconds):
    if n == 0 or totalSeconds == 0:
        return 0

    if sec[n-1] > totalSeconds:
        return maxScore(marks,sec,n-1,totalSeconds)
    
    else:
        return max(marks[n-1] + maxScore(marks,sec,n-1,totalSeconds-sec[n-1]), maxScore(marks,sec,n-1,totalSeconds))


if __name__ == "__main__":
    totalSeconds = 10
    marks = [0, 6, 4, 2, 8]
    sec = [0, 4, 6, 2, 7]
    n = 5
    print(maxScore(marks,sec,n,totalSeconds))