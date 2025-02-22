/*
 * Implemented on 2/22/2025
 * Solved solution, passes all release tests on Neetcode Pro
 * My main issue was that my tail pointer did not point the last element in the array,
 * this caused indexing errors. 
 */

/*
 * Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

 * Your DynamicArray class should support the following operations:
 
 * DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.

 * int get(int i) will return the element at index i. Assume that index i is valid.

 * void set(int i, int n) will set the element at index i to n. Assume that index i is valid.

 * void pushback(int n) will push the element n to the end of the array.

 * int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.

 * void resize() will double the capacity of the array.

 * int getSize() will return the number of elements in the array.

 * int getCapacity() will return the capacity of the array.

 * If we call void pushback(int n) but the array is full, we should resize the array first.
 */
 class DynamicArray {
    private int[] arr;
    private int capacity;
    private int size;
    private int tail;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.capacity = capacity;
        this.size = 0;
        this.tail = -1;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.size == this.capacity) {
            resize();
        }
        this.tail++;
        this.arr[this.tail] = n;
        this.size++;
    }

    public int popback() {
        int lastElt = this.arr[this.tail];
        this.tail--;
        this.size--;
        return lastElt;
    }

    private void resize() {
        this.capacity *= 2;
        int[] doubled = new int[capacity];
        int i;
        for (i = 0; i < this.arr.length; i++) {
            doubled[i] = this.arr[i];
        }
        this.arr = doubled;
        this.tail = i - 1; // tail points to last elt in arr
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
