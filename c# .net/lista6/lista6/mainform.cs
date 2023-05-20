using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lista6
{
    public partial class mainform : Form
    {
        public mainform()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string tekst;
            if (dzienne.Checked)
            {
                 tekst = textBox1.Text + "\r\n" + textBox2.Text + "\r\n" + comboBox1.Text + "\r\n" + dzienne.Text;
            }
            else
                if (zaoczne.Checked)
            {
                 tekst = textBox1.Text + "\r\n" + textBox2.Text + "\r\n" + comboBox1.Text + "\r\n" + zaoczne.Text;
            }
            else         
            
                 tekst = textBox1.Text + "\r\n" + textBox2.Text + "\r\n" + comboBox1.Text;

                childform form = new childform(tekst);
                form.ShowDialog();
            
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Anuluj_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void dzienne_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
