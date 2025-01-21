using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lava002
{
    public class Lavarropa
    {

        public Lavarropa() { }

        public string Lavando(string msg) { return "Lavando" + " " + msg ; }

        public string Centrifuga(int tiempo,string msg) { return "Centrigugando " + tiempo.ToString() + " Min " + msg; }
    
    }
}
