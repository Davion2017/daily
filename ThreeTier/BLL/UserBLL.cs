using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Model;
using DAL;
using System.Data;

namespace BLL
{
    public class UserBLL
    {
        UserDAL userDAL = new UserDAL();
        public bool GetLogin(string name, string password)
        {
            return userDAL.GetLogin(name, password);
        }
        public bool GetReg(User user)
        {
            return userDAL.GetReg(user);
        }
        public DataTable GetAllInfo()
        {
            return userDAL.GetAllInfo();
        }
    }
}
