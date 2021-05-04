#include "stdio.h"

int linear(int arr[], int target, size_t len) {
    for (int i; i <= len; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int * slicer(int arr[], size_t start, size_t end) {
    int *newArr;

}

int recursiveBinary(int arr[], int target, size_t len) {
    if (len > 1 && arr[0] != target) {
        size_t mid = len / 2
        if (arr[mid] == target) {
            return mid;
        } else if (target < arr[mid]) {
            return recursiveBinary()
        }
    } else {
        return -1;
    }
}

int main() {
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    printf("%d%c", linear(arr, 6, 10), '\n');

    return 0;
}
