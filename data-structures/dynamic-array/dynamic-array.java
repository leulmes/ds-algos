/*
 * Implemented on 2/22/2025
 * Solved solution, passes all release tests on Neetcode Pro
 * My main issue was that my tail pointer did not point the last element in the array,
 * this caused indexing errors. 
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
