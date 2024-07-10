
# Bubble Sort 
# Is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# Selection sort
# Is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest)
# element from the unsorted portion of the list and moving it to the sorted portion of the list. 

m_lst_bub = [5,4,181,6,2,3,7,1,123,3,5,-5,78,43,12]
m_lst_srt = [5,4,181,6,2,3,7,1,123,3,5,-5,78,43,12]

def bubble_sort(m_lst):
    for j in range(len(m_lst)):
        for i in range(len(m_lst)-1):
            if m_lst[i+1] < m_lst[i]:
                temp = m_lst[i]
                m_lst[i] = m_lst[i+1]
                m_lst[i+1] = temp
                # print(m_lst)
    return m_lst


def selection_sort(m_lst):
    for j in range(len(m_lst)):
        minpos = j

        for i in range(j, len(m_lst)): # loop to find the smallest number in the list  
            if m_lst[i] < m_lst[minpos]:
                minpos = i

        temp = m_lst[j]  # Reaplaces the position with the smallest num found (minpos)
        m_lst[j] = m_lst[minpos]
        m_lst[minpos] = temp
        # print(m_lst)
    return m_lst


def main():
    bubble_sort(m_lst_bub)
    # selection_sort(m_lst_srt)
    # print(bubble_sort(m_lst_srt) == selection_sort(m_lst_srt))


if __name__ == "__main__":
    main()
