## 概述
基于Django框架开发，同时kvm虚拟化和SDN技术的使用带给了使用者强大的靶机攻防体验。开发目的即一款优秀的专用于比赛的CTF平台，它丰富的比赛内容，灵活的比赛模式以及各项人性化的功能模块满足了比赛举办者的所有要求。然而，同时并不局限于比赛的用途，使用者同样可以用来练习CTF解题和靶机攻防。
## 技术栈

python3.7 + Django 2.1.7 + 10.3.9-MariaDB + REST Framework 3.9.2 + xadmin + Celery + Vue

Restful 风格的 API 应该是前后端分离的最佳实践






## x
superuser:admin@sdutctf123
Django REST framework : admin@sdutctf123

BeginTime: 2019.4.15 ~ now

## 安装说明
xadmin 

验证码模块：https://github.com/mbi/django-simple-captcha

dash: https://gitlab.com/k3oni/pydash-django-app/tree/master

## 临时解决方案（待讨论）
无法修改User中基类中username字段的UNIQUE约束  -->>  注册时后台自动生成随机数进行填充

安全过滤初步想法：通过重载 SessionMiddleware 中间件来实现 或者自定义中间件

## 注意事项

最后部署生产环境要更改 SECRET_KEY 

## 补充
DjangoCon 2008: Reusable Apps： https://www.youtube.com/watch?v=A-S0tqpPga4&feature=youtu.be

测试工具：coverage

API View: GenericAPIView

数据填充：Django  fixture

api验证： JWT  ： http://getblimp.github.io/django-rest-framework-jwt/



