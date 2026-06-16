using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace TRY
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            try
            {
                int[] nro = { 4, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };

                label1.Text += nro[15].ToString();


            }
            catch (Exception x)
            {
                MessageBox.Show(x.Message);
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            StreamReader file = new StreamReader("D:\\CUBOS\\TRY\\TRY\\bin\\Debug\\listado.txt",Encoding.Default);

            try
            {
                
                string line = "";
                while (file.Peek() > 1)
                {
                    line += file.ReadLine() + Environment.NewLine ;
                }
                textBox1.Text = line;
            }
            catch (Exception x)
            {
                MessageBox.Show(x.Message);
            }
            finally
            {
                file.Close();

            }
        }
    }
}
