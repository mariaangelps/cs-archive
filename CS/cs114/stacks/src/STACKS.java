import java.util.Iterator;
public class STACKS {
    public static void main(String[] args) {
        //se crea stack que puede ser AStack como RStack
        //If el resultado de random es menos a 0.5, se crea ASTack, else se crea el RSTACK
        Stack<Integer> stack = Math.random() < 0.5 ? new AStack<Integer>() : new RStack<Integer>();
        //num va a ser inicializado if the args length is 1, else itll be 11
        int num = args.length == 1 ? Integer.parseInt(args[0]) : 11;
        long start, stop;
        System.out.println(stack);
        System.out.println("push");
        start = System.nanoTime();
        for (int i = 0; i < num; ++i) {
            stack.push(i);
            System.out.print(i + " => ");
            for (Integer k : stack) {
                System.out.print(k + " ");
            }
            System.out.println();
        }
        stop = System.nanoTime();
        System.out.println(stop-start);
        Integer j;
        System.out.println("pop");
        start = System.nanoTime();
        while ((j = stack.pop()) != null) {
            System.out.print(j + " => ");
            for (Integer k : stack) {
                System.out.print(k + " ");
            }
            System.out.println();
        }
        stop = System.nanoTime();
        System.out.println(stop-start);
    }
}
interface Stack<E> extends Iterable<E> {
    E pop();
    void push(E data);
}
class AStack<E> implements Stack<E> {
    private class StackIterator<E> implements Iterator<E> {
        public boolean hasNext() {
            return curr > 0;
        }
        public E next() {
            return (E)stack[--curr];
        }
        private int curr = top;
    }
    private void grow() {
        Object[] temp = new Object[stack.length * 2];
        for (int i = 0; i < stack.length; ++i) {
            temp[i] = stack[i];
        }
        stack = temp;
    }
    public Iterator<E> iterator() {
        return new StackIterator<E>();
    }
    public E pop() {
        if (stack.length > 10 && top <= stack.length / 3) {
            shrink();
        }
        E temp = null;
        if (top > 0) {
            temp = (E)stack[--top];
        }
        return temp;
    }
    public void push(E data) {
        if (top >= stack.length) {
            grow();
        }
        stack[top++] = data;
    }
    public void shrink() {
        Object[] temp = new Object[stack.length / 2];
        for (int i = 0; i < temp.length; ++i) {
            temp[i] = stack[i];
        }
        stack = temp;
    }
    private Object[] stack = new Object[10];
    private int top;
}
class RStack<E> implements Stack<E> {
    private class Node<T> {
        private Node(T data) {
            this.data = data;
        }

        private T data;
        private Node<T> next;
    }

    public Iterator<E> iterator() {
        return new Iterator<E>() {
            public boolean hasNext() {
                return curr != null;
            }

            public E next() {
                E temp = curr.data;
                curr = curr.next;
                return temp;
            }

            Node<E> curr = head;
        };
    }

    public E pop() {
        E temp = null;
        if (head != null) {
            temp = head.data;
            head = head.next;
        }
        return temp;
    }

    public void push(E data) {
        Node<E> temp = new Node<E>(data);
        temp.next = head;
        head = temp;
    }

    private Node<E> head;
    //privatee Node<E> tail;
}
