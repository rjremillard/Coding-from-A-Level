#include <stdio.h>

int * merge(int lst[]) {
    size_t len = sizeof(lst) / sizeof(int);

    if (len > 1)
    {
        int mid = len / 2;

        int left[mid];
        for (int i = 0; i <= mid; i++)
        {
            left[i] = lst[i];
        }

        int right[mid];
        for (int i = mid; i <= len; i++)
        {
            right[i] = lst[i];
        }

        int i, j, k = 0;
        int lenLeft = sizeof(left) / sizeof(int);
        int lenRight = sizeof(right) / sizeof(int);

        while (i < lenLeft && j < lenRight)
        {
            if (left[i] < right[i])
            {
                lst[k] = left[i++];
            }
        }

        while (i < lenLeft)
        {
            lst[k++] = left[i++];
        }

        while (j < lenRight)
        {
            lst[k++] = right[j++];
        }
    }
    return lst;
}

void printList(int * start, int len)
{
    for (int i = 0; i < len - 1; i++)
    {
        printf("%d%s", *(start + i), ", ");
    }
    printf("%d%c", *(start + len), '\n');
}

int main() 
{
    int lst[10] = {7, 3, 8, 1, 5, 9, 4, 6, 0, 2};
    int sorted[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    int * answer = merge(lst);

    int correct = 1;
    for (int i; i < 10; i++) 
    {
        if (sorted[i] != *(answer + i)) 
        {
            correct = 0;
        }
    }

    if (correct == 1) 
    {
        printf("%s", "Yay!\n");
    } else {
        printf("%s", "Nope\n");
    }

    printf("%s", "Array:\n");
    printList(answer);

    return 0;
}