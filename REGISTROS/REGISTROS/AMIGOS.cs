using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace REGISTROS
{
    internal class AMIGOS
    {
        List<FICHA> Amis;

        public AMIGOS()
        {
            Amis = new List<FICHA>();


        }

        public void Agregar(FICHA F)
        {
            Amis.Add(F);

        }
        public List<FICHA> Mostrar()
        { return Amis; }

        public void Guardar()
        {
            StreamWriter Archivo = new StreamWriter("Amigos.csv");
            
            foreach(FICHA f in Amis)
            {
                Archivo.WriteLine(f.Legajo.ToString()+";"+ f.Apellido+ ";" + f.Nombre + ";"+f.Email);

            }
            Archivo.Close();
        
        }

    }
}
