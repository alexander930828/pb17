def ins_sort(a):
    n = len(a)

    for i in range(1, n):
        j = i - 1 # 앞에 인덱스
        key = a[i] # 뒤에 인덱스
        while j >= 0 and a[j] > key: # while 문이 외부에서 들어온 리스트의 값을 갱신하지 않기때문에 출력하고자하는 값에 이상X
            a[j+1] = a[j] # 앞에 값이 더 크면 j 값의 위치보다 한칸 오른쪽에 갱신
            j -= 1  # j를 1씩 줄여가면서 계속해서 갱신
        a[j+1] = key # 바꾸지 않아도 된다면 j+1위치에는 이 값을 갱신 만약 j=-1 즉, 비교한 값이 모두 자신보다 클 경우 a[0]에 key 값이 갱신

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)