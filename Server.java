import java.io.*;
import java.net.*;

public class Server extends Thread {

    public static void main(String[] args) throws Exception {
        System.out.println("Server Listening on 8888");
        ServerSocket serverSocket = new ServerSocket(8888);
        serverSocket.setSoTimeout(1000 * 60 * 60);

        Socket server = serverSocket.accept();

        DataInputStream in = new DataInputStream(server.getInputStream());
        try {
            System.out.println(in.readUTF());

        DataOutputStream out = new DataOutputStream(server.getOutputStream());
        out.writeUTF("Welcome and Bye Client!");

            
        } catch(EOFException e){
            System.err.println("Eof Exception occured!");
        }
        
        catch (Exception e) {
            System.err.println("An error has occured!");
        }
        server.close();


    }
}
		