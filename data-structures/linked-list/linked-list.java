class Node {
    private int data;
    private Node next;

    public Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}
class LinkedList {
    private Node head;
    private Node tail;

    public LinkedList() {
        this.head = null;
        this.tail = null; 
    }

    public int get(int index) {
        int count = 0;
        Node curr = this.head;
        while (curr != null && count < index) {
            curr = curr.next;
            count++;
        }
        if (curr != null) {
            // we're in bounds
            return curr.data;
        }
        return -1;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val, null);
        newNode.next = this.head;
        this.head = newNode;
        if (tail == null) {
            this.tail = head;
        }
    }

    public void insertTail(int val) {
        Node newNode = new Node(val, null); 
        // empty list check
        if (tail == null) {
            newNode.next = this.tail;
            this.tail = newNode;
            this.head = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }

    public boolean remove(int index) {
        boolean flag = false;
        Node cur = this.head;
        int curIdx = 0;

        if (cur == null || index >= lstLen()) {
            return false;
        } else {
            if (index == 0) {
                // removing head from 1 elt list vs removing head from multi-elt list
                if (head == tail) {
                    this.head = null;
                    this.tail = null;
                } else {
                    this.head = head.next;
                }
                return true;
            }
            while (cur != null && curIdx < index - 1) {
                cur = cur.next;
                curIdx += 1;
            }
            // 2 conditions: out of bounds or found target
            if (cur == null) {
                return false;
            } else {
                // 2 conditions: remove middle or remove tail
                if (cur.next == this.tail) {
                    this.tail = cur;
                    cur.next = null;
                } else if (cur.next != null) {
                    cur.next = cur.next.next;
                }
                return true;
            }
        }
    }

    private int lstLen() {
        Node curr = this.head;
        int count = 0;
        while (curr != null) {
            count += 1;
            curr = curr.next;
        }
        return count;
    }

    public ArrayList<Integer> getValues() {
        Node curr = this.head;
        ArrayList<Integer> lst = new ArrayList<Integer>();
        while (curr != null) {
            lst.add(curr.data);
            curr = curr.next;
        }
        return lst;
    }
}
