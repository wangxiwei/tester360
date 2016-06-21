# 开发规范

## 代码规范

### PEAR Standard

### FIG (Framework Interop Group) Standards

* **PSR-0 (Autoloading Standard) (Deprecated, use PSR-4 instead)**
 > 感谢 @lifesign 同学指出。FIG 在 2014-10-21 宣布 PSR-4 为类自动加载的推荐标准。如果您的项目不再考虑支持 PHP 5.2 及以下版本，那么请直接使用或升级支持 PSR-4 标准。 

 PSR-0，关于 **类自动加载**。因为 PHP 类加载的机制本质是通过 include 方式达到的，为了避免大量手动 include，需要通过良好的代码组织规范实现自动加载。

 PSR-0 通过时，PHP 5.3 稳定版本才发布没多久，社区内绝大部分开发者支持的仍然为 PHP 5.2 及以下版本（没有 namespace 特性，普遍使用下划线做类隔离），主流开源项目（以 Zend 为盛）也大多遵从 PEAR 标准或自定标准，不过，伴随着 PHP 5.3 的普及（写这段文字的时候 PHP 5.3 已经停止官方支持了）以及 Composer 社区的蓬勃发展，PSR-0 逐步为各大开源项目所接受，取代 PEAR 成为 PHP 开源社区非官方标准（鼓掌）。话说回来，毕竟这是 FIG 组织 2009 年成立推出的第一个规范，当时又大量需要考虑对主流项目的支持，这或许导致了 PSR-0 的一些问题，而这正是自动加载标准修正案（PSR-4）推出的原因。

 > 扩展阅读：
 > * [PSR-0 Standard](http://www.php-fig.org/psr/psr-0/)
 > * [spl_autoload_register()](http://php.net/manual/de/function.spl-autoload-register.php)
 > * [Send PSR-0 to the Standards Farm in the Sky](https://philsturgeon.uk/php/2014/07/19/send-psr0-to-the-standards-farm-in-the-sky/)


* PSR-1 (Basic Coding Standard)
* PSR-2 (Coding Style Guide)
* PSR-3 (Logger Interface)
* PSR-4 (Improved Autoloading)

### PHP Code Sniffer

## 包管理 (Component Management)
 * PEAR
 * Composer
 * PECL
 * Pickle

### 版本命名规范
 * [Sematic Versioning](http://semver.org/)
 * [Software release life cycle](http://en.wikipedia.org/wiki/Software_release_life_cycle)
