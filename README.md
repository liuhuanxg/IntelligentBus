#### 一、项目配置：

1. 项目依赖：项目文件夹中有requirements.txt，此即为项目运行所需配置环境。

    使用pip installl -r requirements.txt进行安装。

2. 配置数据库，数据库使用mysql数据库，在本地新建数据库，然后在settings中进行库名、用户名、密码配置

3. 执行项目迁移

    python manage.py makemigrations

    python manage.py migrate

4. 导入数据文件

    mysql -uroot -p

    use 数据库;

     source  bus.sql

5. 运行项目：

    python manage.py runserver

#### 二、公交线路智推系统，主要包含三个模块：

1. 用户个人中心
2. 公交-站台-路线
3. 后台管理（管理公交信息）

**城市编号from：10000**
**站台编号from：1000001**

**admin管理平台账号：**
账号：admin
密码：admin

**普通用户：**
账号：hello
密码：admin1

**v1.0用户模块**

1. 用户数据表搭建
2. 修改个人信息
3. 修改密码
4. 重置密码（邮箱校验）

**v2.0公交-站台模块** 

1. 在原来数据库基础上稍作改动
2. 添加数据
3. 数据展示，调整格式

**v3.0用户浏览记录**

1. 新建两张数据表：BusHistory和SiteHistory记录用户喜好
2. index html引入百度api，显示北京市地图
3. index展示用户喜好

**v4.0 admin管理平台**

1. 主要使用数据插入模块插入公交和站点信息
2. 附带权限管理可以对管理员进行权限控制

#### **Be careful**：

系统名称暂定为：智能公交系统，修改时对每页的title进行修改
数据库中站台信息较少，可以补充站台信息。



FINISH！