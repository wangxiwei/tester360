# Web 应用服务器 - Apache, Nginx

近几年 Web 应用服务器市场可以说是 Nginx 一个人的舞台，凭借良好的性能表现、稳定可靠的发挥，Nginx 从 Lighttpd 等高性能 Web 应用服务器竞争者中脱颖而出，一路高歌猛进，短短几年时间就拿下了近百分之二十的市场份额。但是凭着历史积累下的庞大用户数，Apache 目前仍然是 [最广为使用的 Web 服务器（根据 NetCraft 2015 年 2 月数据，在全球访问量最大的一百万个网站中 Apache 市场占有率为 50%，二三名分别为 Nginx 21%、IIS 12%）](http://news.netcraft.com/archives/2015/02/24/february-2015-web-server-survey.html)，依然有大量历史长期项目以及更注重 Apache 丰富的功能且对性能要求不那么高的新项目选择并使用 Apache。

因为上述原因，在目前 Nginx 已逐步是多数互联网公司首选的情况下，我们仍包括了 Apache 的内容。

## Apache HTTP Server（简称 Apache）
[**Apache**](http://httpd.apache.org/) 是一个跨平台、采用模块化设计的 Web 服务器，由于其简单高效、稳定安全的特性，被广泛应用于计算机技术的各个领域。

### Apache 命令

```sh
httpd                       # 启动 Apache
httpd -h                    # 显示帮助
httpd -v                    # 显示版本信息
httpd -V                    # 显示版本，编译器版本和配置参数
httpd -t                    # 检查配置文件语法错误
httpd -l                    # 显示编译模块
httpd -L                    # 显示配置指令说明
httpd -f </path/to/config>  # 指定配置文件
httpd -S                    # 显示配置文件中的设定
```


### 一些 Apache 配置、模块

> **粗体部分** - 个人认为可多关注

* Options
    * 符号连接 - FollowSymLinks  
      开启后，服务器将允许在此目录中使用符号连接，Apache 会检查每个请求中是否包含对符号链接的引用，对请求中包含的每个路径做一次 lstat() 系统调用。如考虑安全防护：永远不要允许使用符号链接；如考虑性能：永远使用 Options FollowSysLinks 且绝不使用 Options SysLinkIfOwnerMatch
    * 目录浏览 - Indexes, 建议关闭
* ServerRoot, DocumentRoot
* 网站默认首页文件 - DirectoryIndex
* **虚拟主机 - NameVirtualHost, ServerName, VirutalHost, ServerAlias**
* **.htaccess 支持 - AllowOverride, .htaccess**  
  只在必要目录中启用 AllowOverride（2.4 版本默认关闭）。.htaccess 文件可以极大便利 Apache 参数设置，而无需每次修改都要编辑 Apache 的配置文件（需要重启服务生效），但是也降低了服务器的性能。
* [**工作模式/多处理模块（MPM）**](http://httpd.apache.org/docs/2.4/mpm.html)：
    * 查看当前工作模式：`httpd -l`
    * [Prefork 模式](http://httpd.apache.org/docs/2.4/mod/prefork.html)
        - StartServers: 服务器启动时默认开启的进程数
        - MinSpareServers: 最小的空闲进程数
        - MaxSpareServers: 最大的空闲进程数
        - ServerLimit: 在Apache的生命周期内，限制MaxClients的最大值
        - MaxClients: 最大的并发请求数，最大值不能超过 ServerLimit 设置的值
        - MaxRequestsPerChild: 一个进程可以处理的最多的请求数（进程复用），如请求超过该设置则杀死进程，0表示永不过期。
    * [Worker 模式](http://httpd.apache.org/docs/2.4/mod/worker.html)
        - StartServers: 服务器启动时默认开启的进程数
        - MaxClients: 最大的并发请求数
        - MinSpareThreads: 最小的线程空闲数
        - MaxSpareThreads: 最大的线程空闲数
        - ThreadsPerChild: 每一个进程可以产生的线程数
        - MaxRequestsPerChild: 一个线程可以处理的最多的请求数（线程复用），如请求超过该设置则杀死线程，0表示永不过期。
    * [Event 模式](http://httpd.apache.org/docs/2.4/mod/event.html)
* 日志级别、路径、格式 - [LogLevel](http://httpd.apache.org/docs/2.4mod/core.html#loglevel), [ErrorLog](http://httpd.apache.org/docs/2.4/mod/core.html#errorlog), [CustomLog](http://httpd.apache.org/docs/2.4/mod/mod_log_config.html#customlog)
* 认证，授权与访问控制
    * **Order, Deny, Allow**, [Apache: Access Control](http://httpd.apache.org/docs/2.4/howto/access.html)
    * [Apache: Authentication and Authorization](http://httpd.apache.org/docs/2.4/howto/auth.html)
* SSL 支持 - [mod_ssl](http://httpd.apache.org/docs/2.4/mod/mod_ssl.html)
* 避免 DNS 查询 - HostnameLookups off
* 请求超时 - [Timeout](http://httpd.apache.org/docs/2.4/mod/core.html#timeout)
* 文件包含 - [Include](http://httpd.apache.org/docs/2.4/mod/core.html#include)
* 缓存 - [Cache Guide](http://httpd.apache.org/docs/2.4/caching.html)
* 代理 - Proxy, [mod_proxy](http://httpd.apache.org/docs/2.4/mod/mod_proxy.html)

### 扩展阅读
* [**Apache 中文文档**](http://httpd.apache.org/docs/current/)
* [**Apache: Frequently Asked Questions**](http://wiki.apache.org/httpd/FAQ) - 英文，官方问题汇总，篇幅有点长，建议过一遍
* [**Book: Apache Cookbook 中文版**](http://book.douban.com/subject/3356185/) - 关于 Apache 服务器安装、配置以及日常工作中可能遇到问题的解决办法的参考书
* [**Developerworks: 将 Apache httpd 作为应用开发平台**](http://www.ibm.com/developerworks/cn/opensource/os-cn-apachehttpd/) - Apache 扩展开发快速入门示例


## Nginx

[**Nginx**](http://nginx.org/) ("engine x") 是一个高性能的 HTTP 和反向代理服务器，也是一个 IMAP/POP3/SMTP 邮件代理服务器 。 Nginx 是由 Igor Sysoev 为俄罗斯访问量第二的 Rambler.ru 站点开发的，自发布以来的很长一段时间里，Nginx 为 [Yandex](http://www.yandex.ru/), [Mail.Ru](http://mail.ru/), [VK](http://vk.com/), 以及 [Rambler](http://www.rambler.ru/) 等俄罗斯网站经受住了强大的访问考验。Igor 将源代码以类 BSD 许可证的形式（[2-clause BSD-like license](http://nginx.org/LICENSE)）发布。自 Nginx 发布以来，Nginx 已经因为它的稳定性、丰富的功能集、示例配置文件和低系统资源的消耗而越来越受到各大互联网公司的欢迎。目前国内各大网站都已经部署了 Nginx，如新浪、网易、腾讯等，Nginx 技术在国内日趋火热，越来越多的网站开始部署 Nginx。

-- 源自：http://wiki.nginx.org/NginxChs

### Nginx 命令

```sh
nginx                       # 启动 Nginx
nginx -h                    # 显示帮助
nginx -c </path/to/config>  # 指定一个 Nginx 配置文件，以代替缺省的。
nginx -t                    # 不运行，仅仅测试配置文件语法的正确性。
nginx -v                    # 显示 Nginx 的版本。
nginx -V                    # 显示 Nginx 的版本，编译器版本和配置参数。 
nginx -s reload             # 更改了配置后无需重启 Nginx，平滑重启。
nginx -s stop               # 停止 Nginx
```

### Nginx 常见使用场景/功能

* [Web 服务器](http://nginx.com/resources/admin-guide/web-server/) - 提供虚拟主机服务、地址重写、默认错误页面等
* [反向代理](http://nginx.com/resources/admin-guide/reverse-proxy/) - 反向代理 Apache 服务、PHP-FPM 服务、Memecached 服务等
* [负载均衡](http://nginx.com/resources/admin-guide/load-balancer/) - 将请求根据设定的策略算法分发到一组服务器中的其中一台
* [Web 内容静态缓存](http://nginx.com/resources/admin-guide/caching/) - 缓存后端代理服务器提供的静态或动态内容
* [访问控制](http://nginx.com/resources/admin-guide/restricting-access/) - 通过 auth_basic, limit_req_zone, limit_req, limit_conn, limit_rate 等配置来限制用户访问、访问 IP、并发连接数、带宽使用情况等。


### Nginx 模块

Nginx 的模块从功能角度主要可以分为以下三类，

* **Handler 模块** - 主要负责处理客户端请求并产生待响应内容，比如 ngx_http_static_module 模块，负责客户端的静态页面请求处理并将对应的磁盘文件准备为响应内容输出。
* **Filter 模块）** - 主要负责对输出的内容进行处理，可以对输出进行修改，如 ngx_http_not_modified_filter_module, ngx_http_header_filter_module 模块。
* **Upstream 模块** - 实现反向代理的功能，将真正的请求转发到后端服务器上，如 ngx_http_proxy_module、ngx_http_fastcgi_module 模块。

> Nginx 模块列表： http://wiki.nginx.org/Modules

### Nginx 配置指令

Nginx 配置项指令（Directives）根据作用域/指令上下文（context）可分类如下，

* **main** - Nginx 在运行时与具体业务功能（比如 HTTP 服务或者 Email 服务代理）无关的一些参数，比如工作进程数，运行的用户等。
* **event** - 定义 Nginx 事件工作模式与连接数上限等参数。
* **http** - 与提供 HTTP 服务相关的一些配置参数。如是否使用 keepalive、是否使用gzip进行压缩等。
* **server** - HTTP 服务上支持若干虚拟主机。每个虚拟主机一个对应的 server 配置项，配置项里面包含该虚拟主机相关的配置。在提供 mail 服务的代理时，也可以建立若干 server，每个 server 通过监听的地址来区分。
* **location** - http 服务中，某些特定的 URL 对应的一系列配置项。
* **mail** - 实现 email 相关的 SMTP/IMAP/POP3 代理时，共享的一些配置项（因为可能实现多个代理，工作在多个监听地址上）。

> * Nginx 配置文件说明： [官方示例-英文](http://wiki.nginx.org/ModulesByExample)，[中文详解](http://www.ha97.com/5194.html)
> * Nginx 配置指令列表： [英文](http://nginx.org/en/docs/dirindex.html)，[中文](http://nginx.org/cn/docs/dirindex.html)


### 扩展阅读
* [**Nginx 性能调优 - 英文**](http://nginx.com/blog/tuning-nginx/)
* [**Tengine**](http://tengine.taobao.org/) - Tengine 是由淘宝网基于 Nginx 发起的 Web 服务器项目（完美兼容 Nginx）。它在 Nginx 的基础上，针对大访问量网站的需求，添加了很多高级功能和特性。Tengine 的性能和稳定性已经在大型的网站如淘宝网，天猫商城等得到了很好的检验。
* [**OpenResty**](http://openresty.org/) - OpenResty 通过汇聚各种 Nginx 模块，从而将 Nginx 有效的变成一个强大的 Web 应用服务器。这样，Web 开发人员可以使用 Lua 脚本语言调动 Nginx 支持的各种模块，快速构造出足以胜任 10K+ 并发连接响应的超高性能 Web 应用系统。
* [**Nginx 模块开发 & 原理剖析：Nginx开发从入门到精通**](http://tengine.taobao.org/book/index.html) - 淘宝核心系统服务器平台组同学组织编写的一本关于 Nginx 模块的开发以及它的内部原理的在线书。


##  Web 服务器常用配置

* [Module comparison matrix](http://wiki.nginx.org/ModuleComparisonMatrix) - Nginx, Apache, Lighttpd 模块对应表
* [最小权限原则](http://en.wikipedia.org/wiki/Principle_of_least_privilege) 设置文件、文件夹权限
    * chmod, chown
    * rwx? 755？ - [Linux 文件系统权限 - 英文](http://en.wikipedia.org/wiki/File_system_permissions#Notation_of_traditional_Unix_permissions)
* 单独建立运行用户及用户组
    * Apache - [User](http://httpd.apache.org/docs/current/mod/mod_unixd.html#user), [Group](http://httpd.apache.org/docs/current/mod/mod_unixd.html#group)
    * Nginx - [user](http://nginx.org/en/docs/ngx_core_module.html#user)
* 合理使用浏览器缓存 - Expires, Etag, Cache-Control, Last-Modified
  浏览器缓存（Browser Caching）是为了节约网络的资源、加快浏览速度，浏览器在用户磁盘上对最近请求过的文档进行存储，当访问者再次请求这个页面时，浏览器尝试直接从本地磁盘获取文档内容，加速页面访问速度的一种方法。

  浏览器缓存主要有两种方式，
    * 缓存协商 - Etag, Last-modifie
     缓存协商的方式去服务器端询问页面有没有修改过，没有修改则返回 304 直接使用缓存内容，否则返回新内容
    * 彻底缓存 - Cache-Control，Expires
     彻底缓存的方式在缓存失效之前不再跟服务器交互，直接使用缓存内容

  您可以参考这篇文章了解到更多信息 - [Heroku: Increasing Application Performance with HTTP Cache Headers](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers#cache-prevention)
* 使用压缩 - 节省网络带宽
    * Apache - [mod_deflate](http://httpd.apache.org/docs/2.4/mod/mod_deflate.html), 
    * Nginx - [gzip](http://nginx.org/en/docs/http/ngx_http_gzip_module.html)
* 保持连接 - KeepAlive 参数让服务器和客户端之间在指定一段时间保持同一个连接。这个特性有好处也有坏处，好处是如果客户端发出多个请求，服务端不必每次都花时间去创建连接，坏处是这段时间内即使客户端不再发出新的请求、访问新的页面，这个连接也会被占用，这对服务器资源来说是一种浪费。
    * Apache - [KeepAlive](http://httpd.apache.org/docs/2.4/mod/core.html#keepalive), [KeepAliveTimeout](http://httpd.apache.org/docs/2.4/mod/core.html#keepalivetimeout), [MaxKeepAliveRequests](http://httpd.apache.org/docs/2.4/mod/core.html#maxkeepaliverequests)
    * Nginx - [keepalive](http://nginx.org/r/keepalive), [keepalive_requests](http://nginx.org/r/keepalive_requests), [keepalive_timeout](http://nginx.org/r/keepalive_timeout)
* 配置文件推荐目录结构

    ```sh
    mkdir ./site-available ./site-enabled
    echo 在 site-available 中写好网站配置文件
    cd ../site-enabled
    ln -s ../site-available/xxx.conf
    ```

* 计算进程平均占用内存 (kb) - 以便决定服务器需要多少内存空间（以 Apache 为例）

    ```sh
    ps aux | grep -v grep | awk '/sbin\/httpd/ {sum+=$6;n++}; END {print sum/n}'
    ```

* 地址重写 - URL Rewrite

  > [Tool：Apache 规则转 Nginx 规则](https://github.com/mow/apache2nginx)

    * Apache - [mod_rewirte 模块](http://httpd.apache.org/docs/2.4/rewrite/)
    * Nginx - [ngx_http_rewrite_module 模块](http://nginx.org/en/docs/http/ngx_http_rewrite_module.html)
* 响应头不显示版本信息及操作系统版本信息
    * Apache
        * ServerTokens - 是否在错误页面、目录列表等页面的底部显示服务器操作系统信息
        * ServerSignature - HTTP 头中是否回显 Apache 版本信息
    * Nginx - server_tokens off;
* 关闭不用的模块及功能
    * Apache - 注释掉不用的 LoadModule 配置项
    * Nginx - 编译时确定（Tengine 支持运行时动态加载 HTTP 模块）


### 扩展阅读
* [Tutorial: Top 20 Nginx WebServer Best Security Practices](http://www.cyberciti.biz/tips/linux-unix-bsd-nginx-webserver-security.html)
* [Book: 构建高性能Web站点](http://book.douban.com/subject/3924175/)
* [Book: 高性能网站建设指南](http://book.douban.com/subject/3132277/)
* [Book: 高性能网站建设进阶指南](http://book.douban.com/subject/4719162/)