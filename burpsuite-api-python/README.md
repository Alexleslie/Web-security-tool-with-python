# burpsuite-api-python

+ 利用burpsuite-api 实现python编写extender

+ 利用其接口 实现多种方法，几乎可直接用python控制burpsuite 的流程

+ 这里我只是实现简单的两个功能

  + 获取已经接受或者发出的http/https 的流量包

    + IHttpListener

  + 获取当前正在流经proxy的http/https流量包，且可以对其做出修改，丢弃，转发等操作

    + IProxyListener

      ​