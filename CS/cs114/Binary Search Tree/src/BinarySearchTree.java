//Maria Angel Palacios Sarmiento
//CS 114-006
import java.util.Iterator;
import java.util.Vector;

public class BinarySearchTree<E extends Comparable<? super E>> extends BinaryTree<E> {

    public void insert(E data) {
        Node<E> node = new Node<E>(data);
        root = insert(root, node);
    }

    //Insert Method
    private Node<E> insert(Node<E> currentNode, Node<E> newNode) {
        if (currentNode == null) {
            return newNode;
        } else if (currentNode.data.compareTo(newNode.data) >= 0) {
            currentNode.left = insert(currentNode.left, newNode);
        } else if (currentNode.data.compareTo(newNode.data) < 0) {
            currentNode.right = insert(currentNode.right, newNode);
        }
        return currentNode;
    }
    //Non-Recursive Iterator

    public Iterator<E> iterator() {
        vector = new Vector<E>();
        tracking(root);
        return vector.iterator();
    }

    //Remove method
    public void remove(E data) {
        root = remove(root, data);
    }
    private Node<E> remove(Node<E> currNode, E data) {
        if (currNode == null) {
            return currNode;
        } else if (currNode.data.compareTo(data) > 0) {
            currNode.left = remove(currNode.left, data);
        } else if (currNode.data.compareTo(data) < 0) {
            currNode.right = remove(currNode.right, data);
        } else {
            if (currNode.left == null) {
                return currNode.right;
            } else if (currNode.right == null) {
                return currNode.left;
            }

            Node<E> order = findOrder(currNode);
            currNode.data = order.data;

            currNode.left = remove(currNode.left, currNode.data);
        }
        return currNode;
    }

    private Node<E> findOrder(Node<E> current) {
        current = current.left;
        while (current.right != null) {
            current = current.right;
        }
        return current;
    }

    //search method
    public boolean search(E data) {
        return search(root, data);
    }

    private boolean search(Node<E> currNode, E data) {
        if (currNode == null) {
            return false;
        } else if (currNode.data.compareTo(data) == 0) {
            return true;
        } else if (currNode.data.compareTo(data) > 0) {
            return search(currNode.left, data);
        }
        return search(currNode.right, data);
    }


    //tracking
    private void tracking(Node<E> current) {
        if (current != null) {
            tracking(current.left);
            vector.add(current.data);
            tracking(current.right);
        }
    }

    private Vector<E> vector;
}
