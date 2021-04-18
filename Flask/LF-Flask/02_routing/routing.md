# Routing

## 建立新 route (2 種方法)
> 1. 使用 __Decorator__ ``@obj.route()`` 加入新route
> ``` py
> @app.route(url='/index',
>            methods=['GET', 'POST'],
>            endpoint='route_A')
> def route_1():
>     return render_template('route_1.html')
> ```
> 
> 2. 使用 __Function__ ``obj.add_route_rule()`` 加入新route
> ``` py
> def route_2():
>     return render_template('route_2.html')
>    
> app.add_route_rule(url='/index',
>                    methods=['POST', 'GET'],
>                    view_func=route_2,
>                    endpoint='route_B')
> ```

## 建立新 Regular Expression Converter
### 建立
``` py
class RegexConverter(BaseConverter):
    r"""Customize a Regex for matching the url."""
    def __init__(self):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    @staticmethod
    def to_python(value):
        r"""Transform the regex pattern into python data type."""
        return value

    def to_url(self, value):
        r"""When using url_for() to get url, return the params for the url."""
        return super(RegexConverter, self).to_url(value)
```
### 使用
``` py
app.url_map.converters['new_regex'] = RegexConverter

@app.route('/index/new_regex("\d+"):nid>')
def index(nid):
    return 'index' + nid
```   

   
   

   