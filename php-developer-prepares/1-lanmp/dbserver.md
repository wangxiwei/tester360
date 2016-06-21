# 数据库服务器

## MySQL

### MySQL 分支与变种

* [**MySQL**](http://www.mysql.com/)
* [**MariaDB**](https://mariadb.org/)
* [**Percona Server**](http://www.percona.com/)


### MySQL 知识点

* SQL 基础
    * DDL(Data Definition Language) - 数据定义
        * CREATE - 创建表
        * ALTER - 修改表
        * DROP - 删除表
    * DML(Data Manipulation Language) - 数据操作
        * INSERT - 数据插入
        * DELETE - 数据删除
        * UPDATE - 数据修改
        * SELECT - 数据查询
            * GROUP - 分组
            * JOIN - 连接
            * UNION - 联合
            * 子查询
            * 分页 - LIMIT, OFFSET
    * DCL(Data Control Language) - 数据控制
        * GRANT - 授权
        * REVOKE - 撤销授权
    * 事务(Transactions)
        * ACID 特性
        * COMMIT
        * ROLLBACK
    * 数据提交方式
        * 显式提交 - COMMIT 命令直接完成的提交为显式提交
        * 隐式提交 - SQL 命令间接完成的提交为隐式提交
        * 自动提交 - AUTOCOMMIT ON
    * 范式 &　反范式
* 存储引擎
    * MyISAM
    * InnoDB
* 权限
    * 最小权限原则
    * Grant
    * Revoke
    * 系统表 user, db, host, tables_priv, columns_priv, procs_priv
* 字符集与校对
* 索引
* 约束
    * 外键约束
* 视图
* 查询优化
    * Explain
    * Index Hint
    * 慢查询
* 服务器状态
* 主从分离 & 复制
* 分区表


### MySQL 配置


### 相关工具

* [PHPMyAdmin]()
* [HeidiSQL](http://www.heidisql.com/)
* [Navicat（收费）](http://www.navicat.com/)
* [Sequel Pro](http://www.sequelpro.com/) - Mac OS
* [MySQL Workbench](http://dev.mysql.com/downloads/workbench/)


### 扩展阅读

* [Book: 高性能 MySQL](http://book.douban.com/subject/4241826/)
* [Blog: MySQL Performance Blog](http://mysqlperformanceblog.com)


## MongoDB


### 相关工具

