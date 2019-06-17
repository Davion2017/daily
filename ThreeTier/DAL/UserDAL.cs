using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using Model;
using Common;

namespace DAL
{
    public class UserDAL
    {
        /// <summary>
        /// 检查登录
        /// </summary>
        /// <param name="name"></param>
        /// <param name="password"></param>
        /// <returns></returns>
        public bool GetLogin(string name, string password)
        {
            string sql = "select count(*) from userinfo where userName='" + name + "' and userPassword='" + password + "';";
            if(SqlHelper.ExecuteScalar(sql) > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public bool GetReg(User user)
        {
            string sql = "insert into userinfo(userName, userPassword) values('" + user.UserName + "','" + user.UserPassWord + "');";
            if(SqlHelper.ExecuteNonQuery(sql) > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public DataTable GetAllInfo()
        {
            string sql = "select * from userinfo;";
            return SqlHelper.ExecuteDataTable(sql);
        }
    }
}
