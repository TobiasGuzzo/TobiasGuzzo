using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reloj001
{
    public class RELOJ
    {
        int _hora;
        int _minuto;
        int _segundo;

        public RELOJ() { 
        
            _hora = 0;
            _minuto = 0;
            _segundo = 0;
        
        }
        public RELOJ(int hora, int minuto,int segundo) {
        
            _hora= hora;
            _minuto= minuto;
            _segundo= segundo;
        }

        public int Hora 
        { 
            get { return _hora; }
            set { _hora = value; }
               
        }

        public int Minuto
        {
            get { return _minuto; }

            set
            {
                _minuto = value;







            }
        }

        public int Segundo 
        {
            get { return _segundo; }
            
            set
            {
                if(_segundo + value > 60)
                {
                    Minuto += 1;
                    _segundo = 0;


                }

            }
            
            } 
        

         public static RELOJ operator +(RELOJ A, RELOJ B ) 
          {
              RELOJ x = new RELOJ();
              x._hora = B._hora+ A._hora;
              x._minuto = B._minuto + A._minuto;
              x._segundo = B._segundo + A._segundo;
              return x;

          }
        

        public override string ToString()
        {
            return _hora.ToString() + ":"+ _minuto.ToString()+":" + _segundo.ToString();
        }
    }
}
