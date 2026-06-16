using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reloj001
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RELOJ A = new RELOJ(20,15,30 );
            RELOJ B = new RELOJ();
            B = A;
            label1.Text = B.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RELOJ A = new RELOJ(20, 15, 30);
            RELOJ B = new RELOJ();
            RELOJ C = new RELOJ();
            C = A + B;
            label1.Text = C.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int a = 40;
            int b = 40;
            int c = (a + b) % 60;
            label1.Text = c.ToString();
        }
    }
}
