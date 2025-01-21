using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace REGISTROS
{
    public partial class Form1 : Form
    {
        // List<FICHA> Amigos = new List<FICHA>();

        // int posicion = 0;

        AMIGOS friend;
        public Form1()
        {
            InitializeComponent();
            friend = new AMIGOS();
        }

        private void btnApregar_Click(object sender, EventArgs e)
        {
            FICHA ficha= new FICHA();
            ficha.Legajo = int.Parse(txtLegajo.Text);
            ficha.Apellido = txtApellido.Text;
            ficha.Nombre = txtNombre.Text;
            ficha.Email = txtEmail.Text;
            friend.Agregar(ficha);
           
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = friend.Mostrar();
                }

        private void button2_Click(object sender, EventArgs e)
        {
            friend.Guardar();
        }
    }
}
