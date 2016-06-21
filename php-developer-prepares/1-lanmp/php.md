# PHP

## 各版本主要功能改动
* PHP 5.3 - namespace, closure
* PHP 5.4 - trait, short array syntax
    * http://php.net/manual/en/migration54.new-features.php
* PHP 5.5 - finally, generator
    * http://php.net/manual/en/migration55.new-features.php
* PHP 5.6 - constant expressions, variadic function, argument unpacking, phpdbg
    * http://php.net/manual/en/migration56.new-features.php
* PHP 7.0 - Improved **performance**: PHP 7 is up to twice as fast as PHP 5.6, Consistent 64-bit support, Many fatal errors are now Exceptions, Removal of old and unsupported SAPIs and extensions, The null coalescing operator (??), Combined comparison Operator (<=>), Return Type Declarations, Scalar Type Declarations, Anonymous Classes
    * http://php.net/manual/en/migration70.new-features.php

## PHP 命令


## PHP 知识结构

> * PHP 语言基础请参考 [PHP 官方文档](http://php.net/manual)
> * 关于安全、设计模式等更多内容请参考「设计&开发」相关章节

* [PHP 生命周期](http://www.php-internals.com/book/?p=chapt02/02-01-php-life-cycle-and-zend-engine)
* [PHP FPM (FastCGI Process Manager)](http://php-fpm.org/about/)
* [命令行模式](http://php.net/manual/en/features.commandline.php)
* 语言结构(Language Construct) - language construct is not a function, cannot be called using [variable functions](http://php.net/manual/en/functions.variable-functions.php), such as echo, print, unset(), isset(), empty(), include, require
    * [Stack Overflow: Language Construct vs Function](http://stackoverflow.com/questions/1180184/what-is-the-difference-between-a-language-construct-and-a-built-in-function-in)
* 数组操作（个人认为 PHP 与其他语言对比，强大的数组功能大大简化了开发者对数据的结构类组织工作）
    * 关联数组
    * 多维数组
    * 排序
* 自动加载 - Autoloading
    * __autoload
    * spl_autoload_register()
* 类型比较 - [PHP type comparison tables](http://php.net/manual/en/types.comparisons.php)
    * isset(), empty(), is_null(), boolean : if($x) 函数对变量 $x 进行比较
    * 松散比较 == vs 严格比较 ===
* 魔术方法 - magic method

    > PHP 将所有以 \_\_（两个下划线）开头的类方法保留为魔术方法。所以在定义类方法时，除了上述魔术方法，建议不要以 \_\_ 为前缀。

    * 属性重载
        * __get() - 调用未定义的属性时调用
        * __set() - 对未定义的属性赋值时调用
        * __isset() - 对未定义属性使用 isset()、empty() 方法时被调用
        * __unset() - 对未定义属性使用 unset() 方法时被调用
    * 方法重载
        * __call() - 调用一个不存在的方法时被调用
        * __callStatic() - 调用一个不存在的静态方法时被调用
    * 序列化
        * __sleep() - 序列化对象时被调用
        * __wakeup() - 反序列化对象时被调用
    * 构造函数
        * __construct() - 构造函数，对象初始化时被调用
        * __destruct() - 析构函数，对象释放时被调用
    * 其他
        * __invoke() - 尝试以方法调用的方式调用一个对象时被调用
        * __toString() - 当一个类被尝试当做字符串使用时被调用，返回值只能为字符串，否则触发 PHP 致命错误
        * __clone() - 使用 clone 关键字作对象复制时被调用
        * __set_state() - 使用 var_export() 方法导出类时被调用
        * __debugInfo() - 使用 var_dump() 方法导出类时被调用
* OOP - 面向对象
    * 继承、封装、多态
    * SPL - Standard PHP Library
    * 抽象类 vs 接口
    * 访问控制 - public, private, protected
    * 属性
    * 静态方法、属性
    * 静态延时绑定 - static
    * 常量 vs define
    * 命名空间
    * 反射
    * 类函数 vs 对象函数
    * Final 类
    * Traits - like Partial Class in C#
* OPCode
* 回调、匿名函数和闭包
* 生成器 - [Generator](http://php.net/manual/en/language.generators.overview.php)
    * yield
* heredoc & nowdoc (PHP 5.3.0 新增)
* PDO & mysqlnd
* 错误和异常处理
    * PHP Error
        * trigger_error
        * 将 PHP Error 转为 Exception 处理 - [set_error_handler](http://php.net/manual/en/function.set-error-handler.php)
    * PHP Exception
* Coding Tips - 语言层面编写高性能 PHP 代码 - 单引号比双引号快？ echo 比 print 好？

    > NOTE: 两篇文章都有一段时间没有更新了，不过还是有一定的参考价值

    * [Collection of PHP Performance Benchmarks](http://maettig.com/code/php/php-performance-benchmarks.php)
    * [PHP Benchmark](http://www.phpbench.com/)
* 安全模式 - safe_mode（自 PHP 5.3.0 起废弃并将自 PHP 5.4.0 起移除。）

## 扩展阅读

* [**Book: PHP 和 MySQL Web 开发 - PHP 5.3/2009**](http://book.douban.com/subject/3549421/) - PHP 开发入门最佳选择，主要关注语言本身
* [**Book: 深入PHP 面向对象、模式与实践**](http://book.douban.com/subject/6559267/) - PHP 开发进阶，关注使用面向对象开发、设计模式编写稳定可维护的代码，同时介绍了版本管理(SVN)、持续集成等实践知识
* [**Book: Morden PHP - PHP 5.6/2015**](http://shop.oreilly.com/product/0636920033868.do) - PHP: The Right Way 作者新作，关于 PHP 开发实践的一本书
* [**Github: Awesome PHP**](https://github.com/ziadoz/awesome-php) - PHP 相关库、资源整理
* [**Github: PHP must watch**](https://github.com/phptodayorg/php-must-watch) - PHP 相关视频整理