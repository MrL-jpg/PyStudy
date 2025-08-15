import socket
import threading
import time
from collections import defaultdict

# 配置参数
HOST = '127.0.0.1'
PORT = 8888
CHAT_FILE = "../ChatFile/ChatHistory.txt"
MAX_CLIENTS = 100

class ChatServer:
    def __init__(self):
        """初始化服务器状态"""
        self.clients = {}  # 存储客户端连接 {socket: username}
        self.client_lock = threading.Lock()  # 客户端列表线程锁
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(MAX_CLIENTS)
        print(f"⚡ 聊天服务器已启动 | {HOST}:{PORT}")

    def broadcast(self, message, sender_sock=None):
        """
        向所有客户端广播消息（排除发送者）
        
        参数:
            message: 要广播的消息内容 (bytes)
            sender_sock: 发送消息的客户端socket (可选)
        """
        with self.client_lock:
            for sock, username in list(self.clients.items()):
                if sock != sender_sock:  # 不广播给发送者
                    try:
                        sock.sendall(message)
                    except:
                        self.remove_client(sock)

    def remove_client(self, client_sock):
        """安全移除客户端并通知其他用户"""
        if client_sock in self.clients:
            username = self.clients[client_sock]
            with self.client_lock:
                del self.clients[client_sock]
            try:
                client_sock.close()
            except:
                pass
            leave_msg = f"🚪 用户 [{username}] 已离开聊天室".encode('utf-8')
            self.broadcast(leave_msg)
            print(f"❌ 客户端断开: {username}")
            return username
        return None

    def save_message(self, username, message):
        """将消息保存到历史记录文件"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_entry = f"[{timestamp}] {username}>{message}\n"
        with open(CHAT_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        return log_entry

    def handle_client(self, client_sock, addr):
        """处理单个客户端连接的线程函数"""
        try:
            # 接收并验证用户名
            username = client_sock.recv(1024).decode('utf-8').strip()
            if not username:
                raise ValueError("无效用户名")
            
            # 注册新用户
            with self.client_lock:
                self.clients[client_sock] = username
            
            # 通知新用户加入
            join_notice = f"✅ 用户 [{username}] 加入聊天室".encode('utf-8')
            self.broadcast(join_notice)
            print(f"➕ 新客户端连接: {addr[0]}:{addr[1]} | 用户名: {username}")
            
            # 发送欢迎消息
            welcome_msg = f"欢迎 {username}! 当前在线用户: {len(self.clients)}人".encode('utf-8')
            client_sock.sendall(welcome_msg)
            
            # 持续接收消息
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                    
                # 解析消息内容
                message = data.decode('utf-8')
                if message.lower() == 'exit':
                    break
                
                # 保存并广播消息
                full_msg = f"{username}>{message}".encode('utf-8')
                self.save_message(username, message)
                self.broadcast(full_msg, client_sock)
                
        except ConnectionResetError:
            print(f"⚠️ 客户端强制断开: {addr}")
        except Exception as e:
            print(f"处理客户端错误: {str(e)}")
        finally:
            self.remove_client(client_sock)

    def start(self):
        """启动服务器主循环"""
        try:
            while True:
                client_sock, addr = self.server_socket.accept()
                print(f"🔗 接受来自 {addr[0]}:{addr[1]} 的连接")
                
                # 创建新线程处理客户端
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_sock, addr),
                    daemon=True
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\n🛑 服务器关闭中...")
        finally:
            with self.client_lock:
                for sock in list(self.clients.keys()):
                    sock.close()
            self.server_socket.close()
            print("✅ 服务器已安全关闭")

if __name__ == "__main__":
    server = ChatServer()
    server.start()