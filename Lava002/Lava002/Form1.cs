using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lava002
{
    public partial class Form1 : Form
    {
        Lavarropa Drean;
        DateTime _tiempo; 
        public Form1()
        {
            InitializeComponent();
            Drean= new Lavarropa();
            _tiempo = DateTime.Now;
            this.Text = _tiempo.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TimeSpan _diferencia = DateTime.Now - _tiempo;
            
            label1.Text = Drean.Lavando(Display(_diferencia));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            TimeSpan _diferencia = DateTime.Now - _tiempo;
            
            label1.Text = Drean.Centrifuga(6 , Display( _diferencia));
        }
        private string Display(TimeSpan timeSpan)
        {
            int hora = timeSpan.Hours;
            int minuto = timeSpan.Minutes;
            int sec = timeSpan.Seconds;
            return hora.ToString() + ":" + minuto.ToString() + ":" + sec.ToString();


        }
    }
}
