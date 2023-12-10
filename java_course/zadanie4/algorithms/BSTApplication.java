package algorithms;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BSTApplication extends JFrame {

    private BST<String> bst;
    private TreePanel treePanel;
    private JLabel sizeLabel;

    public BSTApplication() {
        bst = new BST<>();
        initializeUI();
    }

    private void initializeUI() {
        setSize(500, 400);

        treePanel = new TreePanel();
        add(treePanel, BorderLayout.CENTER);

        JPanel controlPanel = new JPanel();
        JTextField inputField = new JTextField(10);
        JButton insertButton = new JButton("Insert");
        JButton removeButton = new JButton("Remove");
        JButton clearButton = new JButton("Clear");

        sizeLabel = new JLabel("Size: 0");
        controlPanel.add(sizeLabel);

        insertButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = inputField.getText();

                if (!value.isEmpty() && value.length() < 5) {
                    bst.insert(value);
                    inputField.setText("");
                    updateUI();

                }
            }
        });

        removeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = inputField.getText();
                if (!value.isEmpty()) {
                    bst.remove(value);
                    updateUI();
                }
            }
        });

        clearButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                bst.clear();
                bst.size=0;
                updateUI();
            }
        });

        controlPanel.add(new JLabel("Value:"));
        controlPanel.add(inputField);
        controlPanel.add(insertButton);
        controlPanel.add(removeButton);
        controlPanel.add(clearButton);

        add(controlPanel, BorderLayout.SOUTH);
    }

    private void updateUI() {
        treePanel.repaint();
        sizeLabel.setText("Size: " + bst.size());
    }

    private class TreePanel extends JPanel {

        private static final int SIDE = 20;
        private static final int LOW = 50;

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            drawTree(g, getWidth() / 2, 30, bst.root, getWidth() / 4);
        }

        private void drawTree(Graphics g, int x, int y, BST<String>.Node node, int xOffset) {
            if (node != null) {
                g.drawOval(x - SIDE, y - SIDE, 2 * SIDE, 2 * SIDE);
                g.drawString(node.getValue(), x - 5, y + 5);

                if (node.left != null) {
                    int xLeft = x - xOffset;
                    int yLeft = y + LOW;
                    g.drawLine(x, y + SIDE, xLeft, yLeft - SIDE);
                    drawTree(g, xLeft, yLeft, node.left, xOffset / 2);
                }

                if (node.right != null) {
                    int xRight = x + xOffset;
                    int yRight = y + LOW;
                    g.drawLine(x, y + SIDE, xRight, yRight - SIDE);
                    drawTree(g, xRight, yRight, node.right, xOffset / 2);
                }
            }
        }
    }


}
