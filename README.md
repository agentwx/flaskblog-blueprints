flaskblog-blueprints
====================


用蓝图实现的flaskblog，用于说明蓝图的基本使用. 这个只是一个简单的例子，为了方便熟悉蓝图(blueprint)使用，目前templates是集中放在一起的，可以分别放入每一个app单独的文件夹，只需要在指定template_folder='templates'。

例如：about = Blueprint('about', __name__,
                        template_folder='templates')

本例子十分简单，不适合使用蓝图，如果有大型的应用的话，建议使用蓝图。如果只是中小型的应用话，可以参考这个结构:
https://github.com/sixu05202004/autotest
