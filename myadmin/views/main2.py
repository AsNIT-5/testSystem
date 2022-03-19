import paramiko
import socket

# 取消校验
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# host, user, password = input("请依次输入主机 用户名 密码，三者用空格隔开：").split(" ")
host = "10.196.110.45"
user = "root"
password = "000000"


# 任务一

def base():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        # 正确值y，错误值z，x其他参数
        x, y, z = client.exec_command("hostnamectl;cat /etc/hosts")
        outcome = y.read().decode("utf-8")
        if "Static hostname: controller" in outcome:
            print("True")
        else:
            print("False")
        if " controller" and " compute" in outcome:
            print("True")
        else:
            print("False")
        print("任务1 题目1检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def yum():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command("cat /etc/yum.repos.d/local.repo")
        outcome = y.read().decode("utf-8")
        if "baseurl=http://10.196.110.34/Competition_2021/iaas/iaas-repo/" in outcome:
            print("True")
        else:
            print("False")
        print("任务1 题目2检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def time():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command("cat /etc/chrony.conf |grep -Ev '^$|#';systemctl status chronyd")
        outcome = y.read().decode("utf-8")
        if "local stratum 10" in outcome:
            print("True")
        else:
            print("False")
        if "Active: active (running)" in outcome:
            print("True")
        else:
            print("False")
        print("任务1 题目3检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def block():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command("lsblk")
        outcome = y.read().decode("utf-8")
        if "20G  0 part" in outcome:
            print("True")
        else:
            print("False")
        print("任务1 题目4检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


# 任务二
def openrc():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command("cat /etc/xiandian/openrc.sh |grep -Ev '^$|#'")
        outcome = y.read().decode("utf-8")
        if "DOMAIN_NAME=demo" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目1检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def mysql():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "systemctl status mariadb;"
            "mysql -uroot -p000000 -e \"show VARIABLES like '%max_connections%';"
            "\";mysql -uroot -p000000 -e \"show VARIABLES like '%max_allowed_packet%';\"")
        outcome = y.read().decode("utf-8")
        if "Active: active (running)" in outcome:
            print("True")
        else:
            print("False")
        if "5000" in outcome:
            print("True")
        else:
            print("False")
        if "31457280" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目2检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def keystone():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "mysql -uroot -p000000 -e 'show databases;';"
            "source /etc/keystone/admin-openrc.sh && openstack service list")
        outcome = y.read().decode("utf-8")
        if "keystone" in outcome:
            print("True")
        else:
            print("False")
        if "keystone" and "identity" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目3检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def glance():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "source /etc/keystone/admin-openrc.sh && openstack-service status|grep glance")
        outcome = y.read().decode("utf-8")
        if "Id=openstack-glance-api.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目4检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def nova():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            " "
            "mysql -uroot -p000000 -e 'show databases;'")
        outcome = y.read().decode("utf-8")
        if "Id=openstack-nova-api.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        if "nova_api" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目5检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def neutron():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "source /etc/keystone/admin-openrc.sh && openstack-service status|grep neutron;"
            "mysql -uroot -p000000 -e 'show databases;'")
        outcome = y.read().decode("utf-8")
        if "Id=neutron-linuxbridge-agent.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        if "neutron" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目6检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def dashoboard():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "curl -L http://controller/dashboard")
        outcome = y.read().decode("utf-8")
        if "Login - OpenStack Dashboard" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目7检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def swift():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "source /etc/keystone/admin-openrc.sh && openstack-service status | grep swift;"
            "source /etc/keystone/admin-openrc.sh && swift stat")
        outcome = y.read().decode("utf-8")
        if "Id=openstack-swift-proxy.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        if "Accept-Ranges: bytes" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目8检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def cinder():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "source /etc/keystone/admin-openrc.sh && openstack-service status | grep cinder;"
            "source /etc/keystone/admin-openrc.sh && cinder list")
        outcome = y.read().decode("utf-8")
        if "Id=openstack-cinder-api.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        if "available | blockvolume | 2" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目9检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def heat():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "source /etc/keystone/admin-openrc.sh && openstack-service status | grep heat")
        outcome = y.read().decode("utf-8")
        if "Id=openstack-heat-api-cfn.service ActiveState=active" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


# 任务三
def glance_admin():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            " source /etc/keystone/admin-openrc.sh && openstack image show cirros")
        outcome = y.read().decode("utf-8")
        if "bare" and "qcow2" and "cirros" and "active" in outcome:
            print("True")
        else:
            print("False")
        print("任务3 题目1检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def openstack_tune():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "cat /etc/nova/nova.conf|grep -Ev '^$|#'")
        outcome = y.read().decode("utf-8")
        if "cpu_allocation_ratio = 4" \
                and "ram_allocation_ratio = 1.5" \
                and "reserved_host_memory_mb = 2048" \
                and "reserved_host_disk_mb = 10240" \
                or "service_down_time=120" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def heat_admin():
    t = input("请输入检测模版类型（flavor、user、network）")
    if t in ["flavor", "user", "network"]:
        if t == "flavor":
            try:
                client.connect(hostname=host, username=user, password=password, timeout=2)
                x, y, z = client.exec_command(
                    "source /etc/keystone/admin-openrc.sh && openstack stack create -t server.yaml test;"
                    "source /etc/keystone/admin-openrc.sh && nova flavor-show 1234;cat /root/server.yaml")
                outcome = y.read().decode("utf-8")
                if "stack_status_reason | Stack CREATE started" in outcome:
                    print("True")
                else:
                    print("False")
                if "| 20" and "| 1234" and "| m1.flavor" and "| 1024" and "| 1" in outcome:
                    print("True")
                else:
                    print("else")
                if "type: OS::Nova::Flavor" and "name: m1.flavor" in outcome:
                    print("True")
                else:
                    print("False")
                print("任务3 题目3检测完毕！")
                client.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("链接失败")
            except socket.timeout:
                print("ssh 无法访问")
        elif t == "user":
            try:
                client.connect(hostname=host, username=user, password=password, timeout=2)
                x, y, z = client.exec_command(
                    "source /etc/keystone/admin-openrc.sh && openstack stack create -t create_user.yaml test-user;"
                    "source /etc/keystone/admin-openrc.sh && openstack user list;"
                    "cat /root/create_user.yaml")
                outcome = y.read().decode("utf-8")
                if "stack_status_reason | Stack CREATE started" in outcome:
                    print("True")
                else:
                    print("False")
                if "| heat-user" in outcome:
                    print("True")
                else:
                    print("else")
                if "type: OS::Keystone::User" and "name: heat-user" in outcome:
                    print("True")
                else:
                    print("False")
                print("任务3 题目3检测完毕！")
                client.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("链接失败")
            except socket.timeout:
                print("ssh 无法访问")
        elif t == "network":
            try:
                client.connect(hostname=host, username=user, password=password, timeout=2)
                x, y, z = client.exec_command(
                    "source /etc/keystone/admin-openrc.sh && openstack stack create -t create_net.yaml test-net;"
                    "source /etc/keystone/admin-openrc.sh && neutron net-show Heat-Network;"
                    "cat /root/create_net.yaml")
                outcome = y.read().decode("utf-8")
                if "stack_status_reason | Stack CREATE started" in outcome:
                    print("True")
                else:
                    print("False")
                if "| Heat-Network" and "| ACTIVE" in outcome:
                    print("True")
                else:
                    print("else")
                if "type: OS::Neutron::Subnet" and "get_resource" and "allocation_pools:" in outcome:
                    print("True")
                else:
                    print("False")
                if "10.20.2.0/24" in outcome:
                    print("True")
                else:
                    print("False")
                print("任务3 题目3检测完毕！")
                client.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("链接失败")
            except socket.timeout:
                print("ssh 无法访问")
        else:
            print("输入错误")
    else:
        print("暂无当前类型检测！")


def swift_glance():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "cat /etc/glance/glance-api.conf|grep -Ev '^$|#'")
        outcome = y.read().decode("utf-8")
        if "default_store=swift" \
                and "swift_store_admin_tenants=service" \
                and "swift_store_user=glance" \
                and "swift_store_container=chinaskill_glance" \
                and "swift_create_container_on_put=True" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def redis():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "cat /etc/glance/glance-api.conf|grep -Ev '^$|#'")
        outcome = y.read().decode("utf-8")
        if "default_store=swift" \
                and "swift_store_admin_tenants=service" \
                and "swift_store_user=glance" \
                and "swift_store_container=chinaskill_glance" \
                and "swift_create_container_on_put=True" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def api():
    print("根据题目要求使用post、get、delete、update等请求实现功能即可得分，注意python版本，用到的包！")


def rabbitmq():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            " rabbitmqctl cluster_status;rabbitmq-plugins list")
        outcome = y.read().decode("utf-8")
        if "[{nodes,[{disc,[rabbit@rabbitmq1]},{ram,[rabbit@rabbitmq3,rabbit@rabbitmq2]}]}" in outcome:
            print("True")
        else:
            print("False")
        if "[E] rabbitmq_management" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


def kafka_cluster():
    try:
        client.connect(hostname=host, username=user, password=password, timeout=2)
        x, y, z = client.exec_command(
            "cd /root/example && ansible-playbook cscc_install.yaml --syntax-check;"
            "cd /root/example && ansible-playbook cscc_install.yaml;"
            "ansible node1,node2,node3 -a \"netstat -ntpl\"; ansible node1,node2,node3 -a \"jps\";"
            "ansible node1,node2,node3 -a \"sh /opt/zookeeper-3.4.14/bin/zkServer.sh status\"")
        outcome = y.read().decode("utf-8")
        if "playbook: cscc_install.yaml" in outcome:
            print("True")
        else:
            print("False")
        if "failed=0||failed=0||failed=0" in outcome:
            print("True")
        else:
            print("False")
        if "2181" and "3888" and "2888" in outcome:
            print("True")
        else:
            print("False")
        if "Kafka" in outcome:
            print("True")
        else:
            print("False")
        if "leader" and "follower" in outcome:
            print("True")
        else:
            print("False")
        print("任务2 题目10检测完毕！")
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("链接失败")
    except socket.timeout:
        print("ssh 无法访问")


if __name__ == "__main__":
    base()  # 主机名和映射
    yum()  # yum配置
    time()  # 时间同步
    # # host, user, password = input("请依次输入主机 用户名 密码，三者用空格隔开：").split(" ")
    # block()  # 分区管理
    openrc()  # openrc脚本文件
    mysql()  # mysql安装及优化
    keystone()  # keystone安装
    glance()  # glance安装
    nova()  # nova安装
    neutron()  # neutron安装
    dashoboard()  # dashboard安装
    swift()  # swift安装
    cinder()  # cinder安装
    heat()  # heat安装
    # kafka_cluster()  # ansible搭建kafka集群
    # rabbitmq() # rabbitmq集群搭建
    # glance_admin()  # 镜像管理
    # openstack_tune()  # openstack参数调优
    # heat_admin()  # heat模版使用
    #swift_glance()  # swift作为glance的后端存储
