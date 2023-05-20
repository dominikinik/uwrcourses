using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _6_2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // dodanie elementów do MenuStrip
            ToolStripMenuItem plikToolStripMenuItem = new ToolStripMenuItem("Plik");
            plikToolStripMenuItem.DropDownItems.Add("Otwórz");
            plikToolStripMenuItem.DropDownItems.Add("Zapisz");
            plikToolStripMenuItem.DropDownItems.Add("Zamknij");
            menuStrip1.Items.Add(plikToolStripMenuItem);

            ToolStripMenuItem edycjaToolStripMenuItem = new ToolStripMenuItem("Edycja");
            edycjaToolStripMenuItem.DropDownItems.Add("Kopiuj");
            edycjaToolStripMenuItem.DropDownItems.Add("Wklej");
            menuStrip1.Items.Add(edycjaToolStripMenuItem);

            // dodanie elementów do ContextMenuStrip
            contextMenuStrip1.Items.Add("Otwórz");
            contextMenuStrip1.Items.Add("Zapisz");
            contextMenuStrip1.Items.Add("Zamknij");

            // dodanie elementów do ToolStrip
            toolStrip1.Items.Add("Nowy");
            toolStrip1.Items.Add("Otwórz");
            toolStrip1.Items.Add("Zapisz");

            // dodanie ToolTip do przycisku na ToolStrip
            toolStripButton1.ToolTipText = "Nowy plik";

            // dodanie elementów do TabControl
            TabPage tabPage1 = new TabPage("Pierwsza");
            tabPage1.Controls.Add(new Label() { Text = "To jest pierwsza strona" });
            TabPage tabPage2 = new TabPage("Druga");
            tabPage2.Controls.Add(new Label() { Text = "To jest druga strona" });
            tabControl1.TabPages.Add(tabPage1);
            tabControl1.TabPages.Add(tabPage2);

            // dodanie elementów do SplitContainer
            splitContainer1.Panel1.Controls.Add(new Label() { Text = "Lewa strona" });
            splitContainer1.Panel2.Controls.Add(new Label() { Text = "Prawa strona" });

            // dodanie elementów do Panel
            panel1.Controls.Add(new Label() { Text = "To jest panel" });

            // dodanie elementów do FlowLayoutPanel
            flowLayoutPanel1.Controls.Add(new Button() { Text = "Przycisk 1" });
            flowLayoutPanel1.Controls.Add(new Button() { Text = "Przycisk 2" });
            flowLayoutPanel1.Controls.Add(new Button() { Text = "Przycisk 3" });
        }
    }
}