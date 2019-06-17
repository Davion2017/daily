using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Data;

namespace Common
{
    public class SqlHelper
    {
        public static string strcon = "Data Source=localhost;Initial Catalog=ST;Integrated Security=True";

        public static int ExecuteScalar(string sql)
        {
            using(SqlConnection conn = new SqlConnection(strcon))
            {
                conn.Open();
                using(SqlCommand cmd = new SqlCommand(sql, conn))
                {
                    return Convert.ToInt32(cmd.ExecuteScalar());
                }
            }
        }

        public static int ExecuteNonQuery(string sql)
        {
            using(SqlConnection conn = new SqlConnection(strcon))
            {
                conn.Open();
                using(SqlCommand cmd = new SqlCommand(sql, conn))
                {
                    return cmd.ExecuteNonQuery();
                }
            }
        }

        public static DataTable ExecuteDataTable(string sql)
        {
            using(SqlConnection conn = new SqlConnection(strcon))
            {
                conn.Open();
                using(SqlCommand cmd = new SqlCommand(sql, conn))
                {
                    DataTable table = new DataTable();
                    using(SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                    {
                        adapter.Fill(table);
                    }
                    return table;
                }
            }
        }

        public static SqlDataReader ExecuteDataReader(string sql)
        {
            SqlConnection conn = new SqlConnection();
            conn.Open();
            using (SqlCommand cmd = new SqlCommand(sql, conn))
            {
                SqlDataReader reader = cmd.ExecuteReader(CommandBehavior.CloseConnection);
                return reader;
            }
        }
    }
}
