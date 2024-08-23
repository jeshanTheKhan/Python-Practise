if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    result = unique_scores[1]
    print(result)