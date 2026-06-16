using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Agenda
{
    public partial class Form1 : Form
    {
        Agenda a;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Agenda a= new Agenda();
            openFileDialog1.Filter = "Archivo de dato(csv,dat)|*.csv;*.dat|Todos los archivos(All)|*.*";
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            a.LLenar(openFileDialog1.FileName, listBox1);


        }

        private void button2_Click(object sender, EventArgs e)
        {
            Agenda a = new Agenda();
            openFileDialog1.Filter = "Archivo de dato(csv,dat)|*.csv;*.dat|Todos los archivos(All)|*.*";
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            a.Mostrar(openFileDialog1.FileName, dataGridView1);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Agenda a = new Agenda();
            openFileDialog1.Filter = "Archivo de dato(csv,dat)|*.csv;*.dat|Todos los archivos(All)|*.*";
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            a.LlenarCombo(openFileDialog1.FileName, comboBox1);

            comboBox1.AutoCompleteSource = AutoCompleteSource.CustomSource; 
            comboBox1.SelectedIndex = 0;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            Persona persona = new Persona();
            a = new Agenda();
            persona = a.TraerFicha(comboBox1.SelectedIndex);
            textBox1.Text = persona.Legajo;
            textBox2.Text = persona.Email;
        }
    }
}
