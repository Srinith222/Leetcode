#include <bits/stdc++.h>
using namespace std;

// The Merge function: Combines two sorted halves
void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp;
    int i = left;      // Pointer for Left half
    int j = mid + 1;   // Pointer for Right half

    // Compare and merge
    while(i <= mid && j <= right) {
        if(arr[i] <= arr[j]) {
            temp.push_back(arr[i++]);
        } else {
            temp.push_back(arr[j++]);
        }
    }

    // Cleanup remaining elements in Left half (if any)
    while(i <= mid) {
        temp.push_back(arr[i++]);
    }

    // Cleanup remaining elements in Right half (if any)
    while(j <= right) {
        temp.push_back(arr[j++]);
    }

    // Copy the merged temp array back into the original array
    for(int k = left; k <= right; k++) {
        arr[k] = temp[k - left];
    }
}

// The recursive Divide function
void mergeSort(vector<int>& arr, int left, int right) {
    if(left >= right) return; // Base case: 1 element is already sorted

    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);      // Sort Left half
    mergeSort(arr, mid + 1, right); // Sort Right half
    merge(arr, left, mid, right);   // Merge them together
}