using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace reloj
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = string.Empty;
            Reloj001 A = new Reloj001(20, 15, 30);
            Reloj001 B = new Reloj001();
            B = A;

            label1.Text += B.ToString();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Reloj001 A = new Reloj001(20, 15, 30);
            Reloj001 B = new Reloj001(04,15, 31);
            Reloj001 C = new Reloj001();
            C = A+B;
            label1.Text = C.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int a = 40;
            int b = 40;
            int c = (a+b)%60;
            label1.Text = c.ToString();
        }
    }
}
