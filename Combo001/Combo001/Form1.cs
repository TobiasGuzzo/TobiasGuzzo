using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Data.OleDb;

namespace Combo001
{
    public partial class Form1 : Form
    {
        SqlConnection Cnx;
        SqlCommand Cmd;
        string CadenaCnx = "Data Source=localhost;Initial Catalog=TestIndexado;Integrated Security=True";


        public Form1()
        {
            InitializeComponent();

            Cnx = new SqlConnection(CadenaCnx);
            Cnx.Open();


            AutoCompleteStringCollection combData = new AutoCompleteStringCollection();
            getData(combData);
            CmbAlumno.AutoCompleteCustomSource = combData;
            CmbAlumno.DataSource = combData;
            CmbAlumno.DisplayMember = "nm_persona";
        }


        public void getData(AutoCompleteStringCollection combo)
        {
            string Sql = "Select nm_persona, dni_persona from Tabla1 order by nm_persona";

            Cmd = new SqlCommand(Sql,Cnx);

            SqlDataReader Dtr = Cmd.ExecuteReader();


            while (Dtr.Read()) { 
             combo.Add(Dtr["dni_persona"].ToString() +", " + Dtr["nm_persona"].ToString());

            }
            Cmd.Dispose();

        }

        private void CmbAlumno_KeyPress(object sender, KeyPressEventArgs e)
        {
            //CmbAlumno.DroppedDown = true;
            if (char.IsControl(e.KeyChar))
            {
                // Aca va el Codigo
                CargarDatos(CmbAlumno.Text);
                return;
            }
            string str = CmbAlumno.Text.Substring(0, CmbAlumno.SelectionStart) + e.KeyChar;
            Int32 index = CmbAlumno.FindStringExact(str);
            if (index == -1)
            {
                index = CmbAlumno.FindString(str);
            }
            this.CmbAlumno.SelectedIndex = index;
            this.CmbAlumno.SelectionStart = str.Length;
            this.CmbAlumno.SelectionLength = this.CmbAlumno.Text.Length - this.CmbAlumno.SelectionStart;

            e.Handled = true;

        }

        public void CargarDatos(string data)
        {
            CmbAlumno.DroppedDown = true;

            string[] s = data.Split(',');
            SqlDataReader Dr;
            SqlCommand Cm;
            string strsql =  "SELECT  *  FROM Tabla1  Where (nm_persona ='" + s[0] + "') AND (dni_persona ='" + s[1].Trim() + "')";
            SqlConnection cone = new SqlConnection("Data Source=localhost;Initial Catalog=TestIndexado;Integrated Security=True");
            cone.Open();
            Cm = new SqlCommand(strsql, cone);
            Dr =  Cm.ExecuteReader();

                if (Dr.Read())
                {

                    txtLegajo.TextAlign = HorizontalAlignment.Right;
                    txtLegajo.Text =Dr["id_persona"].ToString();
                    txtApellido.Text = Dr["nm_persona"].ToString();
                    txtNombre.Text = Dr["dni_persona"].ToString();
                    //txtDocumento.Text = reader.IsDBNull["Documento"] ? 0 :reader["Documento"].ToString();
                    //if (!reader.IsDBNull(reader.GetOrdinal("NroDocumento")))
                   // txtAsistencia.Text = Dr["Asistencia"].ToString();
                    //txtEmail.Text = Dr["Email"].ToString();
                    /* 
                     * if (reader["Sexo"].ToString() == "Femenino")
                        rdbFemenino.Checked = true;
                    else
                        rdbMasculino.Checked = true;
                    */
                }
            
                Cm.Dispose();
            cone.Close();
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
