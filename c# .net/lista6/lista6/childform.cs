using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lista6
{
    public partial class childform : Form
    {
        private string parametr { get; set; }
        public childform(string parametr)
        {
            InitializeComponent();
            this.parametr = parametr;
            this.textBox1.Text = parametr;
        }

        private void childform_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();   
        }

       


        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }
    }
}
