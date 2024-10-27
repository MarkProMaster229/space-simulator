using System;
using System.Windows.Forms;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent(); // Вызов конструктора из Designer.cs
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Логика при загрузке формы
        }

        private void ButtonSend_Click(object sender, EventArgs e)
        {
            textBoxLog.AppendText("Отправлено: " + textBoxInput.Text + Environment.NewLine);
            textBoxInput.Clear();
        }
    }
}