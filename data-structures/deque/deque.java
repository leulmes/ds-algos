// Need a Doubly LL for O(1) removal at the end
class Node {
    int data;
    Node next;
    Node prev;

    public Node(int data, Node next, Node prev) {
        this.data = data;
        this.next = next;
        this.prev = prev;
    }
}
class Deque {
    Node head;
    Node tail;

    public Deque() {
        this.head = null;
        this.tail = null;
    }

    public boolean isEmpty() {
        if (this.head == null) 
            return true;
        return false;
    }

    public void append(int value) {
        // add to end of queue
        Node newNode = new Node(value, null, null);
        if (head == null) {
            // Empty queue case
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }

    public void appendleft(int value) {
        // add to beginning of queue
        Node newNode = new Node(value, null, null);
        if (this.head == null) {
            // queue is empty
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
        }
    }

    public int pop() {
        if (this.head != null) {
            int lastElt = this.tail.data;
            if (this.tail.prev == null) {
                // only 1 elt 
                this.head = null;
                this.tail = null;
                return lastElt;
            } else {
                Node tmp = this.tail.prev;
                this.tail.prev.next = null;
                this.tail.prev = null;
                this.tail = tmp;
                return lastElt;
            }
        }
        return -1;
    }

    public int popleft() {
        if (this.head != null) {
            Node tmp = this.head.next;
            int firstElt = this.head.data;
            if (head.next == null) {
                // 1 elt deque
                this.head = null;
                this.tail = null;
            } else {
                this.head.next.prev = null;
                this.head.next = null;
                this.head = tmp;
            }
            return firstElt;
        }
        return -1;
    }
}
