using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace lista7
{
    public partial class Form1 : Form
    {
        private Timer timer = new Timer();
        private int centerX, centerY, radius;
        public Form1()
        {
            InitializeComponent();
            this.Paint += new PaintEventHandler(Form1_Paint);
            this.Resize += new EventHandler(Form1_Resize);
            timer.Interval = 1000;
            timer.Tick += new EventHandler(timer_Tick);
            timer.Start();
        }

        void Form1_Paint(object sender, PaintEventArgs e)
        {
            DrawClock(e.Graphics);
        }

        void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        void timer_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void DrawClock(Graphics g)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // get the current time
            DateTime now = DateTime.Now;
            int hour = now.Hour;
            int minute = now.Minute;
            int second = now.Second;

            // calculate the center and radius of the clock face
            centerX = this.ClientSize.Width / 2;
            centerY = this.ClientSize.Height / 2;
            radius = (int)(Math.Min(centerX, centerY) * 0.9);

            // draw the clock face
            g.FillEllipse(Brushes.White, centerX - radius, centerY - radius, radius * 2, radius * 2);
            g.DrawEllipse(Pens.Black, centerX - radius, centerY - radius, radius * 2, radius * 2);

            // draw the hour hand
            double hourAngle = (hour % 12 + minute / 60.0) * 30 * Math.PI / 180;
            int hourLength = (int)(radius * 0.5);
            int hourX = centerX + (int)(hourLength * Math.Sin(hourAngle));
            int hourY = centerY - (int)(hourLength * Math.Cos(hourAngle));
            g.DrawLine(Pens.Black, centerX, centerY, hourX, hourY);

            // draw the minute hand
            double minuteAngle = (minute + second / 60.0) * 6 * Math.PI / 180;
            int minuteLength = (int)(radius * 0.8);
            int minuteX = centerX + (int)(minuteLength * Math.Sin(minuteAngle));
            int minuteY = centerY - (int)(minuteLength * Math.Cos(minuteAngle));
            g.DrawLine(Pens.Black, centerX, centerY, minuteX, minuteY);

            // draw the second hand
            double secondAngle = second * 6 * Math.PI / 180;
            int secondLength = (int)(radius * 0.9);
            int secondX = centerX + (int)(secondLength * Math.Sin(secondAngle));
            int secondY = centerY - (int)(secondLength * Math.Cos(secondAngle));
            g.DrawLine(Pens.Red, centerX, centerY, secondX, secondY);
            g.FillEllipse(Brushes.Red, secondX - 2, secondY - 2, 4, 4);
        }
    }
}
 
