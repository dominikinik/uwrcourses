using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace jakasbiblioteka
{
    public class AUTO 
    {
        public string nazwa;

        private string rok;

        internal int iloscwalscicieli;

        protected string perrejestracja;
        public AUTO(string nazwa,string rok, int iloscwalscicieli,string perrejestracja)
        {
            this.nazwa = nazwa;
            this.rok = rok;
            this.iloscwalscicieli = iloscwalscicieli;
            this.perrejestracja = perrejestracja;


        }
    }
}
