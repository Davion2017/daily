using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ServerConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            const int BufferSize = 8192;
            Console.WriteLine("Server is running……");
            IPAddress ip = new IPAddress(new byte[] { 127, 0, 0, 1 });
            TcpListener listener = new TcpListener(ip, 8500);
            listener.Start();
            Console.WriteLine("Start Listening");
            
            TcpClient remoteClient = listener.AcceptTcpClient();
            Console.WriteLine("Client Connected! {0}<--{1}", remoteClient.Client.LocalEndPoint, remoteClient.Client.RemoteEndPoint);


            NetworkStream streamToClient = remoteClient.GetStream();
            do
            {
                byte[] buffer = new byte[BufferSize];
                int bytesRead = streamToClient.Read(buffer, 0, BufferSize);
                Console.WriteLine("Reading data, {0} bytes ...", bytesRead);

                string msg = Encoding.Unicode.GetString(buffer, 0, bytesRead);
                Console.WriteLine("Received: {0}", msg);
            } while (true);
            

            Console.WriteLine("\n\n输入\"Q\"键退出。");
            ConsoleKey key;
            do
            {
                key = Console.ReadKey(true).Key;
            } while (key != ConsoleKey.Q);
        }
    }
}
