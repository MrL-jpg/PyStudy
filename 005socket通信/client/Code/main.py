'''
@author: eureka
@file: main.py
@time: 2021/01/01
@brief:网络聊天室程序——客户端
'''
import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 8888

# 获取用户名
with open("../ChatFile/ChatHistory.txt", "r+", encoding="utf-8") as f:
    user_name = input("请创建您的用户名: ")
    # 检查用户是否存在
    if user_name not in f.read():
        f.write(f"user_name:{user_name}\n")


# 连接到Socket服务器
def socket_init(host="127.0.0.1", port=8888):
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((host, port))
        print("服务器连接成功")
        return client_sock
    except ConnectionRefusedError:
        print("无法连接到服务器：服务器未启动或地址错误")
    except Exception as e:
        print(f"连接错误: {str(e)}")
    return None


# 接收服务端消息的线程函数
def rcv_msg(client_sock):
    while True:
        try:
            # 设置超时以定期检查连接状态
            client_sock.settimeout(1.0)
            data = client_sock.recv(1024)
            if not data:
                print("服务器已断开连接")
                break

            msg = data.decode("utf-8")
            print(f"\n{msg}")  # 使用换行符确保不会覆盖输入提示

            # 保存消息
            with open("../ChatFile/ChatHistory.txt", "a", encoding="utf-8") as f:
                f.write("\n" + msg)
        except socket.timeout:
            # 超时属于正常现象，继续循环
            continue
        except ConnectionResetError:
            print("连接被服务器重置")
            break
        except Exception as e:
            print(f"接收消息出错: {str(e)}")
            break


# 主客户端运行函数
def run_client(client_sock, user_name):
    try:
        client_sock.send(user_name.encode("utf-8"))
        print(f"欢迎您 {user_name}，按回车发送消息，输入\"exit\"退出程序\n")

        # 启动接收消息的线程
        receiver = threading.Thread(target=rcv_msg, args=(client_sock,), daemon=True)
        receiver.start()

        while True:
            try:
                prompt = f"{user_name}> "
                msg = input(prompt)

                # 检查退出指令
                if msg.lower() in ["exit", "quit"]:
                    client_sock.send("exit".encode("utf-8"))
                    print("断开连接...")
                    break

                # 发送消息到服务器
                full_msg = f"{user_name}> {msg}"
                client_sock.send(full_msg.encode("utf-8"))

                # 短暂等待确保接收线程不会覆盖输入提示
                time.sleep(0.05)
            except KeyboardInterrupt:
                print("\n用户中断，退出程序")
                break
            except Exception as e:
                print(f"发送消息出错: {str(e)}")
                break
    finally:
        client_sock.close()
        print("连接已关闭")


# 主程序
if __name__ == "__main__":
    client_socket = socket_init(HOST, PORT)
    if client_socket:
        run_client(client_socket, user_name)