if __name__ == '__main__':
    n = int(input())
    integer_list =  tuple(map(int, input().split()))
    
    t = hash(integer_list) 
    print(t)