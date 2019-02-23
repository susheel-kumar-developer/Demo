def inversionBase(n): 
    
    octalValue=0 ;   
    i = 0; 
    while (n != 0): 
        octalValue += n % 8; 
        n = int(n / 8); 
        i += 1;       
    return octalValue

if __name__ == '__main__':
    N = int(input())
    drive_sequence=[0] * N
    main_sequence = input().rstrip().split(',')
    for i in range(N):
        drive_sequence[i]=inversionBase(int(main_sequence[i]))
    inversion=0    
    for i in range(N):
        for j in range(i+1, N):
            if drive_sequence[i] > drive_sequence[j]:
                inversion += 1
    print(int(inversion), end = '')
