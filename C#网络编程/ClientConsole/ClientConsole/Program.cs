using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ClientConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Client is running……");

            //单客户端连接服务端
            TcpClient client = new TcpClient();
            try
            {
                client.Connect("localhost", 8500);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.WriteLine("Server Connected!\n{0}-->{1}", client.Client.LocalEndPoint, client.Client.RemoteEndPoint);

            //string msg = "\"Welcome To TraceFact.Net\"";
            NetworkStream streamToServer = client.GetStream();

            ConsoleKey key;
            Console.WriteLine("Menu: S - Send, X - Exit");
            do
            {
                key = Console.ReadKey(true).Key;
                if(key == ConsoleKey.S)
                {
                    Console.Write("Input the message：");
                    String msg = Console.ReadLine();
                    byte[] buffer = Encoding.Unicode.GetBytes(msg);     // 获得缓存
                    streamToServer.Write(buffer, 0, buffer.Length);     // 发往服务器
                    Console.WriteLine("Sent: {0}", msg);
                }
            } while (key != ConsoleKey.X);

            

            //多客户端连接服务端
            //TcpClient client;
            //for (int i = 0; i < 2; i++)
            //{
            //    try
            //    {
            //        client = new TcpClient();
            //        client.Connect("localhost", 8500);
            //    }
            //    catch (Exception ex)
            //    {
            //        Console.WriteLine(ex.Message);
            //        return;
            //    }
            //    Console.WriteLine("Server Connected!\n{0}-->{1}", client.Client.LocalEndPoint, client.Client.RemoteEndPoint);
            //}


            Console.WriteLine("\n\n输入\"Q\"键退出。");
            //ConsoleKey key;
            do
            {
                key = Console.ReadKey(true).Key;
            } while (key != ConsoleKey.Q);
        }
    }
}
