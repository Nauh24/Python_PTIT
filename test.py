def is_prime(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def find_prime(num):
    # giam = num -1
    # while not is_prime(giam):
    #     giam -= 1

    # tang = num +1
    # while not is_prime(tang):
    #     tang +=1

    # return giam if num-giam<=tang -num else tang
    tang=0
    giam=0
    while not is_prime(num+tang):
        tang+=1
    while not is_prime(num-giam):
        giam+=1
    return min(tang,giam)

def step_prime(arr):
    step =0
    for num in arr:
        if not is_prime(num):
            num = find_prime(num)
            step=max(step,num)
    return step

if __name__=="__main__":
    N = int(input())
    A = list(map(int,input().split()))
    print(step_prime(A))

'''
8
13 5 8 7 9 15 26 34
'''
