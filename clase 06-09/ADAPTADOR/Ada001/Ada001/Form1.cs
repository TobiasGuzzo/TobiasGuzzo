using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ada001
{
    public partial class Form1 : Form
    {
        string CadenaCnx = "Data Source=localhost;Initial Catalog=Colegio;Integrated Security=True";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                //string ConString = @"data source=LAPTOP-ICA2LCQL\SQLEXPRESS; database=StudentDB; integrated security=SSPI";
                using (SqlConnection connection = new SqlConnection(CadenaCnx))
                {
                    SqlDataAdapter da = new SqlDataAdapter("select * from Alumnos ", connection);

                    //Using Data Table
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    //The following things are done by the Fill method
                    //1. Open the connection
                    //2. Execute Command
                    //3. Retrieve the Result
                    //4. Fill/Store the Retrieve Result in the Data table
                    //5. Close the connection

                    // Console.WriteLine("Using Data Table");
                    listBox1.Items.Add("Usando el Data Table");
                    //Active and Open connection is not required
                    //dt.Rows: Gets the collection of rows that belong to this table
                    //DataRow: Represents a row of data in a DataTable.
                    foreach (DataRow row in dt.Rows)
                    {
                        //Accessing using string Key Name
                        listBox1.Items.Add(row["Apellido"] + ",  " + row["Nombre"] + ",  " + row["Email"]);
                        //Accessing using integer index position
                        //Console.WriteLine(row[0] + ",  " + row[1] + ",  " + row[2]);
                    }

                    listBox1.Items.Add("---------------");

                    //Using DataSet
                    DataSet ds = new DataSet();
                    da.Fill(ds, "Alumnos"); //Here, the datatable student will be stored in Index position 0
                    listBox1.Items.Add("Using el Data Set");

                    //Tables: Gets the collection of tables contained in the System.Data.DataSet.
                    //Accessing the datatable from the dataset using the datatable name
                    foreach (DataRow row in ds.Tables["Alumnos"].Rows)
                    {
                        //Accessing the data using string Key Name
                        
                        listBox1.Items.Add(row["Apellido"] + ",  " + row["Nombre"] + ",  " + row["Email"]);
                        //Accessing the data using integer index position
                        //Console.WriteLine(row[0] + ",  " + row[1] + ",  " + row[2]);
                    }

                    //Accessing the datatable from the dataset using the datatable index position
                    //foreach (DataRow row in ds.Tables[0].Rows)
                    //{
                    //    Console.WriteLine(row["Name"] + ",  " + row["Email"] + ",  " + row["Mobile"]);
                    //}
                }
            }
            catch (Exception ex)
            {   
                listBox1.Items.Add("OOPs, something went wrong.\n" + ex);

            }

           // Console.ReadKey();
        }
    }
    }

