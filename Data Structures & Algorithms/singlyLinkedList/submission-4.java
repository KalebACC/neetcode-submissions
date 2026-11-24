class LinkedList {

    class Node{
        int value;
        Node next;
        
        Node(int value, Node next)
        {
            this.value = value; 
            this.next = next;
        }

        Node (int value)
        {
            this(value,null);
        }
    }
    int size;
    Node head;
    Node tail;

    public LinkedList() {
        this.size = 0;
        this.head = null;
        this.tail = head;
    }

    public int get(int index) {
        if (index >= size || index < 0 ) return -1;


        Node curr = head;
        for (int i=0; i < index; i++)
        {
            curr = curr.next;
        }
        return curr.value;
    }

    public void insertHead(int val) {
        
        if (head == null)
        {
            Node newNode = new Node(val,null);
            head = newNode;
            tail = newNode;
            size++;
            return;
        }

        Node newNode = new Node(val,head);
        head = newNode;
        size++;
    }

    public void insertTail(int val){
        
        if (tail == null){
            Node newNode = new Node(val,null);
            head = newNode;
            tail = newNode;
            size++;
            return;
        }

        Node newNode = new Node(val,null);
        tail.next = newNode;
        tail = newNode;
        size++;
    }

    public boolean remove(int index) {
        if (index >= size || index < 0) return false;
        if (index == 0) 
        {
        head = head.next;
        size--;

        if (size == 0) {
            tail = null;
        }

        return true;
        }

        Node curr = head;
        for (int i=0; i < index-1; i++)
        {
            curr = curr.next;
        }
        
        if (curr.next == tail) tail = curr;

        curr.next = curr.next.next;
        size--;
        return true;
        
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node curr = head;
        for (int i = 0; i < size; i++)
        {
            values.add(curr.value);
            curr = curr.next;
        }
        return values;
    }
}
