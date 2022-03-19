# testSystem

------部署到服务器需自建一个文件------
[uwsgi]
#配置和nginx连接的socket连接
socket=127.0.0.1:8080
#配置项目路径，项目的所在目录
chdir=/www/wwwroot/m.asnit.top/
#配置wsgi接口模块文件路径,也就是wsgi.py这个文件所在的目录
wsgi-file=myobject/wsgi.py
#配置启动的进程数
processes=4
#配置每个进程的线程数
threads=2
#配置启动管理主进程
master=True
#配置存放主进程的进程号文件
pidfile=uwsgi.pid
#配置dump日志记录
daemonize=uwsgi.log
------------网站配置文件添加------------
location / {
  include uwsgi_params;
  uwsgi_pass 127.0.0.1:8080;  #端口要和uwsgi里配置的一样
  uwsgi_param UWSGI_SCRIPT myobject.wsgi;  #wsgi.py所在的目录名+.wsgi
  uwsgi_param UWSGI_CHDIR /www/wwwroot/m.asnit.top/; #项目路径
}
location /static/ {
  alias /www/wwwroot/m.asnit.top/static/; #静态资源路径
}
