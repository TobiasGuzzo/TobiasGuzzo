using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Collections;

namespace Agenda
{
    internal class Agenda
    {
         List<Persona> Amigos = new List<Persona>(); 

        public Agenda() { }

        public void LLenar(string archivo, ListBox lista)
        {
            StreamReader lector = new StreamReader(archivo,Encoding.Default);
            lector.ReadLine();
            
            while (lector.Peek()>1) 
            { 
               lista.Items.Add(lector.ReadLine());
            }

            lector.Close();
        }

        private void Separar(string linea)
        {
            Persona persona = new Persona();
            string[] campo = linea.Split(new char[] { ';' });
            persona.Legajo = campo[0];
            persona.Apellido= campo[1];
            persona.Nombre= campo[2];
            persona.Email= campo[3];
            
            Amigos.Add(persona);
        }

        public void Mostrar(string archivo, DataGridView grilla)
        {
            StreamReader lector = new StreamReader(archivo, Encoding.Default);
            lector.ReadLine();

            while (lector.Peek() > 1)
            {
               Separar(lector.ReadLine());
            }
            grilla.DataSource = Amigos;
            lector.Close();
        }

        public void LlenarCombo(string archivo, ComboBox lista)
        {
            StreamReader lector = new StreamReader(archivo, Encoding.Default);
            lector.ReadLine();

            while (lector.Peek() > 1)
            {
                string[] C =lector.ReadLine().Split(';');
                lista.Items.Add(C[1] + ", " + C[2]);
                Persona p = new Persona();
                p.Legajo = C[0];
                p.Apellido= C[1];
                p.Nombre= C[2];
                p.Email= C[3];
                Amigos.Add(p);

            }
            lector.Close();
        }
        
        public Persona TraerFicha(int posicion)
        {
           Persona persona = new Persona();
           persona = Amigos[posicion];
           return persona;


        }
    }
}
