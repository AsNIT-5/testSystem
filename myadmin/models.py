from django.db import models
from datetime import datetime

'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


# 用户账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)  # 账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=1)  # 状态:1正常/2禁用/9删除
    score = models.FloatField(default=0)  # 分数
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'nickname': self.nickname,
                'password_hash': self.password_hash, 'password_salt': self.password_salt, 'status': self.status,
                'score': self.score,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "user"


# 管理员用户管理
class AdminUser(models.Model):
    username = models.CharField(max_length=50)  # 账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=6)  # 状态:2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'nickname': self.nickname,
                'password_hash': self.password_hash, 'password_salt': self.password_salt, 'status': self.status,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "adminuser"


class Subject(models.Model):
    title = models.CharField(max_length=50)  # 标题
    content = models.TextField()  # 内容
    score = models.FloatField(default=0)  # 分数
    command = models.TextField()  # 检测命令
    # 检测结果
    result1 = models.CharField(max_length=255)
    result2 = models.CharField(max_length=255)
    result3 = models.CharField(max_length=255)
    result4 = models.CharField(max_length=255)
    result5 = models.CharField(max_length=255)
    result6 = models.CharField(max_length=255)
    result7 = models.CharField(max_length=255)
    result8 = models.CharField(max_length=255)
    result9 = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间

    def toDict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content,
                'score': self.score, 'command': self.command, "result1": self.result1, "result2": self.result2,
                "result3": self.result3, "result4": self.result4, "result5": self.result5, "result6": self.result6,
                "result7": self.result7, "result8": self.result8, "result9": self.result9,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "subject"


class Time(models.Model):
    time = models.DateTimeField(default=datetime.now)  # 时间
    describe = models.CharField(max_length=255)

    def toDict(self):
        return {'id': self.id, 'time': self.time.strftime('%Y-%m-%d %H:%M:%S'), 'describe': self.describe}

    class Meta:
        db_table = "time"


class Standard(models.Model):
    s_id = models.IntegerField()
    standard = models.CharField(max_length=255)
    weight = models.FloatField(default=1)  # 权重，默认为1

    def toDict(self):
        return {'id': self.id, 's_id': self.s_id, 'standard': self.standard, 'weight': self.weight}

    class Meta:
        db_table = "standard"


# 日志管理
class Log(models.Model):
    t_user = models.CharField(max_length=255)
    t_subject = models.CharField(max_length=255)
    status = models.IntegerField(default=1)  # 状态:2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 't_user': self.t_user, 't_subject': self.t_subject, 'status': self.status,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'), }

    class Meta:
        db_table = "log"
