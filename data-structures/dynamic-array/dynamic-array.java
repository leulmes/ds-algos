/* Implemented this on 2/21/2025
 * Completed the Dynamic Array
 * challenge on Neetcode Pro
 * */

class DynamicArray {
    private int[] arr;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.capacity = capacity;
        this.size = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.size == this.arr.length) {
            resize();
        }
        this.arr[this.arr.length - 1] = n;
        this.size++;
    }

    public int popback() {
        int lastElt = this.arr[this.arr.length - 1];
        this.arr[arr.length - 1] = 0;
        this.size--;
        return lastElt;
    }

    private void resize() {
        capacity *= 2;
        int[] doubled = new int[capacity];
        for (int i = 0; i < arr.length; i++) {
            doubled[i] = arr[i];
        }
        arr = doubled;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return capacity;
    }
}
