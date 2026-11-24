class DynamicArray {
    int arr[];
    int size;
    int end;
    int capacity;
    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.size = 0;
        this.end = -1;
        this.capacity = capacity;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (end+1 >= capacity){
            resize();
        }

        arr[++end] = n;
        size++;
    }

    public int popback() {
        size--;
        return arr[end--];
        
    }

    private void resize() {
        this.capacity *= 2;
        int[] newArr = new int[capacity];
        for (int i = 0; i < size; i++){
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
