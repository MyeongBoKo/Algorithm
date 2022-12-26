for _ in range(int(input())):
    m_num = 0
    m_name = ''
    for _ in range(int(input())):
        num, name = input().split()
        if int(num) > m_num:
            m_num = int(num)
            m_name = name
    print(m_name)
