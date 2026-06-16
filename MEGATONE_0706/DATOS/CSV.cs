using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ENTIDADES;
using System.IO;
using System.Text.RegularExpressions;
using System.ComponentModel.Design;

namespace DATOS
{
    public class CSV
    {
        List<PRODUCTOS> productos;
        List<DETALLE_FACTURA> detalle_facturas;
        public CSV() {

            productos = new List<PRODUCTOS>();
            detalle_facturas = new List<DETALLE_FACTURA>();

        }

        public PRODUCTOS Cortar_Linea(string linea)
        {
            PRODUCTOS p = new PRODUCTOS();
            string[] C = linea.Split(';');
            p.Codigo = Convert.ToInt32(C[0]);
            p.Marca = C[1];
            p.Nombre = C[2];
            p.Precio = Convert.ToDouble(C[3]);
            p.Tamanio = Convert.ToDouble(C[4]);
            return p;


        }

        public void LeerArchivo(string archivo)
        {
            PRODUCTOS p = new PRODUCTOS();
            StreamReader st = new StreamReader(archivo, Encoding.Default);

            st.ReadLine();

            while (st.Peek() > 1)
            {
                string line = st.ReadLine();
                p = Cortar_Linea(line);
                productos.Add(p);
            }

            st.Close();

        }


        public DETALLE_FACTURA CortarDetalle(string linea)
        {
            DETALLE_FACTURA dETALLE = new DETALLE_FACTURA();

            string[] C = linea.Split(';');

            dETALLE.Factura = Convert.ToInt32(C[0]);
            dETALLE.Producto = Convert.ToInt32(C[1]);
            dETALLE.Cantidad = Convert.ToInt32(C[2]);
            
            return dETALLE;

        }
            
        
        public void LeeerDetalle(string archivo)
        {
            DETALLE_FACTURA dETALLE = new DETALLE_FACTURA();

            StreamReader st = new StreamReader(archivo, Encoding.Default);

            st.ReadLine();

            while(st.Peek() >1)
            {

                string line = st.ReadLine();
                dETALLE = CortarDetalle(line);
                detalle_facturas.Add(dETALLE);



            }

            st.Close();

        }

        public List<PRODUCTOS> MostrarProductos()
        { return productos; }

        public List<DETALLE_FACTURA> MostrarDetalle()
        { return detalle_facturas;}
        
        public List<PRODUCTOS> qryMarcas(string marca)
        {

            var Query = from producto in productos
                        where producto.Marca == marca
                        select producto;
            return Query.ToList();

        }

        public List<PRODUCTOS> qryPrecio(double precio )
        {
            var Query = from producto in productos
                        where producto.Precio >= precio
                        select producto;

            return Query.ToList();
        }
        public Int32 CantidadProductos()
        { return productos.Count; }


        public List<PRODUCTOS> Sort_Precio()
        {
            var Query = from producto in productos
                        orderby producto.Precio ascending
                        select producto;

            return Query.ToList();
        }
        public List<PRODUCTOS> EntrePrecio(double inicial, double   final)
        {
            var Query = from producto in productos
                        where producto.Precio >= inicial && producto.Precio <= final
                        select producto;

            return Query.ToList();



        }
        public List<DETALLE_FACTURA> MostrarFactura(int nrofactura) 
        {
            var query = from detalle in detalle_facturas
                        join producto in productos
                        on detalle.Producto equals producto.Codigo
                        where detalle.Factura == nrofactura
                        select new DETALLE_FACTURA
                        {
                            Factura = detalle.Factura,
                            Producto = producto.Codigo,
                            Cantidad = detalle.Cantidad,
                            Descripcion = producto.Nombre,
                            Precio = producto.Precio,
                            Importe = (producto.Precio * detalle.Cantidad)
                        };

            
         return query.ToList();
        }

    }
}
