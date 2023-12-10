package algorithms;




public class BST<T extends Comparable<T>> implements Dictionary<T> {



    public class Node {
        Node left, right;
        T value;

        Node(T value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        public T getValue() {
            return value;
        }
    }



    public Node root;
    public int size;

    public BST() {
        this.root = null;
        this.size = 0;
    }

    @Override
    public boolean search(T x) {
        return searchRecursive(root, x);
    }

    private boolean searchRecursive(Node node, T x) {
        if (node == null) {
            return false;
        }
        int compareResult = Integer.compare(Integer.parseInt(x.toString()), Integer.parseInt(node.value.toString()));

        if (compareResult < 0) {
            return searchRecursive(node.left, x);
        } else if (compareResult > 0) {
            return searchRecursive(node.right, x);
        } else {
            return true;
        }
    }

    @Override
    public void insert(T x) {
        if (x == null) {
            throw new IllegalArgumentException("NULL");
        }
        root = insertRecursive(root, x);
        size++;
    }

    private Node insertRecursive(Node node, T x) {
        if (node == null) {
            return new Node(x);
        }

        int compareResult = Integer.compare(Integer.parseInt(x.toString()), Integer.parseInt(node.value.toString()));
        System.out.println(compareResult);

        if (compareResult < 0) {
            node.left = insertRecursive(node.left, x);
        } else if (compareResult > 0) {
            node.right = insertRecursive(node.right, x);
        }
        if(compareResult == 0){size--;}
        return node;
    }

    @Override
    public void remove(T x) {
        if (x == null) {
            throw new IllegalArgumentException("NULL");
        }
        if(search(x)){size--;}
        root = removeRecursive(root, x);

    }
    private Node removeRecursive(Node node, T x) {
        if (node == null) {
            return null;
        }

        int compareResult = Integer.compare(Integer.parseInt(x.toString()), Integer.parseInt(node.value.toString()));

        if (compareResult < 0) {
            node.left = removeRecursive(node.left, x);
        } else if (compareResult > 0) {
            node.right = removeRecursive(node.right, x);
        } else {
            if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            }

            node.value = minValue(node.right);
            node.right = removeRecursive(node.right, node.value);
        }


        return node;
    }


    private T minValue(Node node) {
        T minValue = node.value;
        while (node.left != null) {
            minValue = node.left.value;
            node = node.left;
        }
        return minValue;
    }

    @Override
    public T min() {
        if (root == null) {
            throw new IllegalStateException("NULL");
        }
        return minValue(root);
    }

    @Override
    public T max() {
        if (root == null) {
            throw new IllegalStateException("NULL");
        }
        return maxValue(root);
    }

    private T maxValue(Node node) {
        T maxValue = node.value;
        while (node.right != null) {
            maxValue = node.right.value;
            node = node.right;
        }
        return maxValue;
    }

    public int size() {
        return size;
    }

    public void clear() {
        root = null;
        size = 0;
    }
}
