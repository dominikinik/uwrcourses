
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class BinaryTreeNode<T>
    {
        public T Value { get; set; }
        public BinaryTreeNode<T> left { get; set; }
        public BinaryTreeNode<T> right { get; set; }
        public BinaryTreeNode(T value)
        {
            Value = value;
            left = null;
            right = null;
        }
        public IEnumerable<T> DFS()
        {
            yield return Value;
            if (this.left != null)
            {
                foreach (var nodeValue in left.DFS())
                {
                    yield return nodeValue;
                }
            }
            if (this.right != null)
            {
                foreach (var nodeValue in right.DFS())
                {
                    yield return nodeValue;
                }
            }
            

        }
        public IEnumerable<T> BFS()
        {
            Queue<BinaryTreeNode<T>> queue = new Queue<BinaryTreeNode<T>>();
            queue.Enqueue(this);
            while (queue.Count > 0)
            {
                BinaryTreeNode<T> current = queue.Dequeue();
                yield return current.Value;
                if (current.left != null)
                {
                    queue.Enqueue(current.left);
                }
                if (current.right != null)
                {
                    queue.Enqueue(current.right);
                }
            }


        }
    }
        internal class Program
        {
            static void Main(string[] args)
            {
                BinaryTreeNode<int> root = new BinaryTreeNode<int>(1);
                root.left = new BinaryTreeNode<int>(2);
                root.right = new BinaryTreeNode<int>(3);
                root.left.left = new BinaryTreeNode<int>(4);
                root.left.right = new BinaryTreeNode<int>(5);
                root.right.left = new BinaryTreeNode<int>(6);
                root.right.right = new BinaryTreeNode<int>(7);

                
                foreach (int value in root.DFS())
                {
                    Console.Write(value + " ");
                }
                

                
                foreach (int value in root.BFS())
                {
                    Console.Write(value + " ");
                }
            }
        }
    
}

