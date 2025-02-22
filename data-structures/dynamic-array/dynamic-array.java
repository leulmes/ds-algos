class DynamicArray {
    private int[] arr;
    private int capacity;
    private int size;
    private int currIdx;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.capacity = capacity;
        this.size = 0;
        this.currIdx = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.size == capacity) {
            resize();
        }
        this.arr[currIdx] = n;
        this.size++;
        this.currIdx++;
    }

    public int popback() {
        int lastElt = this.arr[this.currIdx];
        this.arr[currIdx] = 0;
        this.currIdx--;
        this.size--;
        return lastElt;
    }

    private void resize() {
        capacity *= 2;
        int[] doubled = new int[capacity];
        int i;
        for (i = 0; i < arr.length; i++) {
            doubled[i] = arr[i];
        }
        arr = doubled;
        currIdx = i;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return capacity;
    }
}
