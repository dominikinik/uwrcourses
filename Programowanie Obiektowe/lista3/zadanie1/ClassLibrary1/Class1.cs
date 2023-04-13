using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class Lista<T>
    {
        private class Node
        {
            public T value;
            public Node next;
            public Node prev;

            public Node(T value)
            {
                this.value = value;
                this.next = null;
                this.prev = null;
            }
        }

        private Node head;
        private Node tail;
        private int count;

        public Lista()
        {
            this.head = null;
            this.tail = null;
            this.count = 0;
        }

        public void push_front(T elem)
        {
            Node node = new Node(elem);

            if (head == null)
            {
                head = node;
                tail = node;
            }
            else
            {
                node.next = head;
                head.prev = node;
                head = node;
            }

            count++;
        }

        public void push_back(T elem)
        {
            Node node = new Node(elem);

            if (tail == null)
            {
                head = node;
                tail = node;
            }
            else
            {
                node.prev = tail;
                tail.next = node;
                tail = node;
            }

            count++;
        }

        public T pop_front()
        {
            if (head == null)
            {
                throw new InvalidOperationException("Lista jest pusta");
            }

            T elem = head.value;

            if (head == tail)
            {
                head = null;
                tail = null;
            }
            else
            {
                head = head.next;
                head.prev = null;
            }

            count--;
            return elem;
        }

        public T pop_back()
        {
            if (tail == null)
            {
                throw new InvalidOperationException("Lista jest pusta");
            }

            T elem = tail.value;

            if (head == tail)
            {
                head = null;
                tail = null;
            }
            else
            {
                tail = tail.prev;
                tail.next = null;
            }

            count--;
            return elem;
        }

        public bool is_empty()
        {
            return count == 0;
        }
    }
}
