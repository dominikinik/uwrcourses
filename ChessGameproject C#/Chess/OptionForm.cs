using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Chess
{
    public partial class OptionForm : Form
    {
        public string SelectedOption { get; private set; } // Właściwość do przechowywania wyboru

        public OptionForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SelectedOption = "Queen"; // Przypisz wartość wyboru do SelectedOption
            DialogResult = DialogResult.OK; // Ustaw DialogResult na OK
            Close(); // Zamknij okno dialogowe
        }

        private void OptionForm_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            SelectedOption = "Rook"; // Przypisz wartość wyboru do SelectedOption
            DialogResult = DialogResult.OK; // Ustaw DialogResult na OK
            Close(); // Zamknij okno dialogowe
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SelectedOption = "Bishop"; // Przypisz wartość wyboru do SelectedOption
            DialogResult = DialogResult.OK; // Ustaw DialogResult na OK
            Close(); // Zamknij okno dialogowe
        }

        private void button4_Click(object sender, EventArgs e)
        {
            SelectedOption = "Knight"; // Przypisz wartość wyboru do SelectedOption
            DialogResult = DialogResult.OK; // Ustaw DialogResult na OK
            Close(); // Zamknij okno dialogowe
        }
    }
}
