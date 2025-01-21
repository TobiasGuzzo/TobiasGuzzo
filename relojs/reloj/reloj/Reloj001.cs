using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reloj
{
    internal class Reloj001
    {
        int _hora;
        int _minuto;
        int _segundo;

        public Reloj001() { 
            _hora = 0;
            _minuto = 0;
            _segundo = 0;

        }
        public Reloj001(int hora, int minuto, int segundo)
        {
            _hora = hora;
            _minuto = minuto;
            _segundo = segundo;
        }

        public int hora { 
            get { return _hora; } 
            set { _hora = value; }
        
        }

        public int minuto
        {
            get { return _minuto; }

            set { _minuto = value;
                  if (value + _minuto > 60) {
                    _hora += 1;
                    _minuto = 0;
                  } else
                {
                    _minuto += 1;
                }
            }

        }

        public int segundo
        {
            get { return _segundo; }
            set { _segundo = value;
                if (value + _segundo > 60)
                {
                    minuto += 1;
                    _segundo = 0;
                }
                else
                {
                    segundo += 1;
                }
            }

        }

        public static Reloj001 operator +(Reloj001 B, Reloj001 A ) {
        
            Reloj001 x = new Reloj001 ();
            x._hora = B._hora + A._hora;
            x._minuto = B._minuto + A._minuto;
            x._segundo = B._segundo + A._segundo;  
            return x;
        }

        public override string ToString()
        {
            return _hora.ToString() + ":" + _minuto.ToString() + ":" + _segundo.ToString();
        }
    }
}
