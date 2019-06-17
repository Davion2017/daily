using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using BLL;
using Model;

namespace ThreeTier
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        UserBLL userBLL = new UserBLL();
        User user = new User();
        private void Button1_Click(object sender, EventArgs e)
        {
            user.UserName = textBox1.Text;
            user.UserPassWord = textBox2.Text;
            if(userBLL.GetLogin(user.UserName, user.UserPassWord))
            {
                MessageBox.Show("登录成功");
            }
            else
            {
                MessageBox.Show("登录失败");
            }
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            user.UserName = textBox1.Text;
            user.UserPassWord = textBox2.Text;
            if(userBLL.GetReg(user))
            {
                MessageBox.Show("注册成功");
            }
            else
            {
                MessageBox.Show("注册失败");
            }
        }
    }
}
